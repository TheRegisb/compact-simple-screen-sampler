#!/usr/bin/python3

# Copyright (c) 2023 Régis Berthelot

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

import traceback
from sys import stderr
from os import name as os_name

from PySide6.QtCore import (Qt, Signal, QRect, QPoint)
from PySide6.QtGui import (QGuiApplication, QColorConstants, QColor, QCursor, QScreen, QKeyEvent, QMouseEvent, QImage)
from PySide6.QtWidgets import (QWidget, QMainWindow)

from app.utils.Maths import average_qimage_rgb
from app.widgets.Images import (ImageRoiSelector, SingleImage)


class ColorPicker(QWidget):
    colorSample = Signal(QColor)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        QGuiApplication.setOverrideCursor(Qt.CrossCursor)
        self.grabMouse()
        self.grabKeyboard()

    def close(self):
        self.releaseMouse()
        self.releaseKeyboard()
        QGuiApplication.restoreOverrideCursor()
        QMainWindow().show()
        super().close()

    # QT Override
    def keyPressEvent(self, event: QKeyEvent) -> None:
        """
        Close the widget on Escape key press.
        """
        key = event.key()
        if key == Qt.Key_Escape:
            self.close()

    @staticmethod
    def get_active_screen() -> QScreen:
        """
        Finds the screen that currently contains the cursor.
        :return: The screen that contains the cursor, or the primary screen otherwise.
        """
        app = QGuiApplication
        cursor_pos = QCursor.pos()

        for screen in app.screens():
            screen_rect = screen.geometry()
            if screen_rect.contains(cursor_pos):
                active_screen = screen
                break
        else:
            print('Warning: Could not find the screen containing the cursor', file=stderr)
            active_screen = app.primaryScreen()
        return active_screen

    @staticmethod
    def get_relative_cursor_position(screen: QScreen) -> QPoint:
        """
        Get the position of the cursor relative to a screen.
        :param screen: Screen to check the position against.
        :return: The relative position of the cursor.
        """
        global_mouse_pos = QCursor.pos()
        mouse_screen_geometry = screen.geometry()
        return global_mouse_pos - mouse_screen_geometry.topLeft()

    @staticmethod
    def is_pressed(event: QMouseEvent, button: Qt.MouseButton) -> bool:
        """
        Check if a mouse button have been pressed during a mouse event.
        """
        return event.buttons() & button == button

    def pick_screen_color(self) -> QColor:
        """
        Method that throws an exception unless implemented by a child class.
        """
        raise NotImplementedError('Error: pick_screen_color must be implemented by its subclasses')


class PixelColorPicker(ColorPicker):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.desktop_covers = None
        # As Windows doesn't support mouse grab outside the app's window, we plaster the screen(s) with widget(s)
        if os_name == 'nt':
            self.desktop_covers = []
            for screen in QGuiApplication.screens():
                self.desktop_covers.append(SingleImage(screen.grabWindow(0).toImage(), screen))
                self.desktop_covers[-1].showFullScreen()

    def close(self):
        if self.desktop_covers is not None:
            for widget in self.desktop_covers:
                widget.close()
            self.desktop_covers = None
        super().close()

    # QT Override
    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Emits the color of the pixel under the cursor on left button press then close the widget. Immediately closes
        the widget on right or middle mouse button press.
        """
        if self.is_pressed(event, Qt.LeftButton):
            try:
                self.colorSample.emit(self.pick_screen_color())
            except Exception as e:  # Board exception catch, we cannot let the program hang/crash during input grab
                traceback.print_exc()
                print(f'Error: Unexpected exception during picking due to {e} -- releasing mouse', file=stderr)
            finally:
                self.close()
        elif self.is_pressed(event, Qt.RightButton) or self.is_pressed(event, Qt.MiddleButton):
            self.close()

    def pick_screen_color(self) -> QColor:
        """
        Pick the color of the pixel under the cursor.
        :return: The color of the pixel under the cursor, or pure-black on failure.
        """
        screen = self.get_active_screen()
        mouse_pos = self.get_relative_cursor_position(screen)
        image = screen.grabWindow(0).toImage()

        if image.rect().contains(mouse_pos):
            return QColor(image.pixel(mouse_pos))
        else:
            print('Warnings: Cursor is outside of the active screen', file=stderr)
            return QColorConstants.Black


class RegionColorPicker(ColorPicker):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.roiSelector = []
        # As Windows doesn't support mouse grab outside the app's window, we plaster the screen(s) with widget(s)
        if os_name == 'nt':
            for screen in QGuiApplication.screens():
                self.roiSelector.append(self.create_roi_selector(screen))
                self.roiSelector[-1].showFullScreen()

        self.screen = None
        self.ptStart = None
        self.ptEnd = None
        self.drawingStarted = False
        self.image = None

    def close(self):
        for widget in self.roiSelector:
            widget.close()
        self.roiSelector = None
        super().close()

    # QT Override
    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Records the starting point of the selection rectangle on left click.
        Closes the widget on right or middle button press.
        """
        if self.is_pressed(event, Qt.LeftButton):
            self.screen = self.get_active_screen()
            self.image = self.screen.grabWindow(0).toImage()
            if os_name != 'nt':
                self.roiSelector.append(self.create_roi_selector(self.get_active_screen()))
                self.roiSelector[0].showFullScreen()
            self.ptStart = self.get_relative_cursor_position(self.screen)
            self.drawingStarted = True
        if self.is_pressed(event, Qt.RightButton) or self.is_pressed(event, Qt.MiddleButton):
            self.close()

    # QT Override
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Updates the ending point of the selection rectangle and draw its outline on the visualization widget.
        """
        if self.drawingStarted:
            self.ptEnd = self.get_relative_cursor_position(self.screen)
            rect = QRect(
                self.ptStart.x(),
                self.ptStart.y(),
                (self.ptEnd.x() - self.ptStart.x()),
                (self.ptEnd.y() - self.ptStart.y())
            )
            self.get_active_roi_selector().update_roi(rect)

    # QT Override
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """
        Emits the average color of the selected region when the left mouse button is released then close the widget.
        """
        if event.button() == Qt.LeftButton:
            self.colorSample.emit(self.pick_screen_color())
            self.close()

    def pick_screen_color(self) -> QColor:
        """
        Extracts the selected region and compute its average color while displaying a wait cursor.
        :return: The average color of the selected region or pure-black on failure.
        """
        try:
            QGuiApplication.setOverrideCursor(Qt.WaitCursor)
            rect = self.image.rect().intersected(QRect(
                self.ptStart.x(),
                self.ptStart.y(),
                (self.ptEnd.x() - self.ptStart.x()),
                (self.ptEnd.y() - self.ptStart.y())
            ))
            roi = self.image.copy(rect)
            return self.compute_rgb_average(roi)
        except Exception as e:  # Board exception catch, we cannot let the program hang/crash during input grab
            traceback.print_exc()
            print(f'Error: Unable to compute the average color of the region because of: {e}', file=stderr)
            return QColorConstants.Black
        finally:
            QGuiApplication.restoreOverrideCursor()

    @staticmethod
    def compute_rgb_average(image: QImage) -> QColor:
        """
        Computes the average color an entire QImage.
        """
        avg_rgb = average_qimage_rgb(image)
        return QColor(avg_rgb[0], avg_rgb[1], avg_rgb[2])

    @staticmethod
    def create_roi_selector(screen: QScreen) -> ImageRoiSelector:
        """
        Create an ImageRoiSelector for a given screen.
        :param screen: Screen to be copied and displayed on.
        :return: A widget ready to be displayed.
        """
        image = screen.grabWindow(0).toImage()
        return ImageRoiSelector(image, screen)

    def get_active_roi_selector(self) -> ImageRoiSelector:
        """
        Get the ImageRoiSelector widget that was selector for sampling.
        :return: The active widget.
        """
        return next((widget for widget in self.roiSelector if widget.screen() == self.screen), self.roiSelector[0])
