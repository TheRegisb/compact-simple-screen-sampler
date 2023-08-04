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

from statistics import mean

from PySide6.QtWidgets import (QWidget, QMainWindow)
from PySide6.QtGui import (QGuiApplication, QColorConstants, QColor, QPixmap, QCursor, QPainter, QFont, QPen)
from PySide6.QtCore import (Qt, Signal, QRect)

from widgets.Images import ImageRoiSelector

from utils.Maths import averageQImageRGB

class ColorPicker(QWidget):
    colorSample = Signal(QColor)

    def __init__(self, parent=None):
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


    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Escape:
            self.close()


    def getActiveScreen(self):
        app = QGuiApplication
        cursorPos = QCursor.pos()
        activeScreen = None

        for screen in app.screens():
            screenRect = screen.geometry()
            if (screenRect.contains(cursorPos)):
                activeScreen = screen
                break
        else:
            println('Warning: Could not find the screen containing the cursor')
            activeScreen = app.primaryScreen()
        return activeScreen
            

    def getRelativeMousePosition(self, screen):
        globalMousePos = QCursor.pos()
        mouseScreenGeometry = screen.geometry()
        return globalMousePos - mouseScreenGeometry.topLeft()


    def isPressed(self, event, button):
        return event.buttons() & button == button


    def pickScreenColor(self):
        raise NotImplementedError('Error: pickScreenColor must be implemented by its subclasses')


class PixelColorPicker(ColorPicker):
    def mousePressEvent(self, event):
        if self.isPressed(event, Qt.LeftButton):
            try:
                self.colorSample.emit(self.pickScreenColor())
            except Exception as e:
                print('Error: Unexpected exception during picking -- releasing mouse')
                print(e)
            finally:
                self.close()
        elif self.isPressed(event, Qt.RightButton) or self.isPressed(event, Qt.MiddleButton):
            self.close()


    def pickScreenColor(self):
        screen = self.getActiveScreen()
        mousePos = self.getRelativeMousePosition(screen)
        image = screen.grabWindow(0).toImage()

        if image.rect().contains(mousePos):
            return QColor(image.pixel(mousePos))
        else:
            return QColorConstants.Black
            

class RegionColorPicker(ColorPicker):
    def __init__(self, event):
        super().__init__(event)
        self.roiSelector = None
        self.screen = None
        self.ptStart = None
        self.ptEnd = None
        self.drawingStarted = False
        self.image = None


    def close(self):
        if self.roiSelector is not None:
            self.roiSelector.close()
            self.roiSelector = None        
        super().close()


    def mousePressEvent(self, event):
        if self.isPressed(event, Qt.LeftButton):
            self.screen = self.getActiveScreen()
            self.image = self.screen.grabWindow(0).toImage()
            if self.roiSelector == None:
                self.roiSelector = ImageRoiSelector(self.image, self.screen)
            self.roiSelector.showFullScreen()
            self.ptStart = self.getRelativeMousePosition(self.screen)
            self.drawingStarted = True
        if self.isPressed(event, Qt.RightButton) or self.isPressed(event, Qt.MiddleButton):
            self.close()


    def mouseMoveEvent(self, event):
        if self.drawingStarted:
            self.ptEnd = self.getRelativeMousePosition(self.screen)
            rect = QRect(
                self.ptStart.x(),
                self.ptStart.y(),
                (self.ptEnd.x() - self.ptStart.x()),
                (self.ptEnd.y() - self.ptStart.y())
            )
            self.roiSelector.updateRoi(rect)


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.colorSample.emit(self.pickScreenColor())
            self.close()


    def pickScreenColor(self):
        try:
            QGuiApplication.setOverrideCursor(Qt.WaitCursor)
            rect = self.image.rect().intersected(QRect(
                self.ptStart.x(),
                self.ptStart.y(),
                (self.ptEnd.x() - self.ptStart.x()),
                (self.ptEnd.y() - self.ptStart.y())
            ))
            roi = self.image.copy(rect)
            avgColor = self.computeRGBAverage(roi)
        except Exception as e:
            print('Error: Unable to compute the average color of the region')
            print(e)
            avgColor = QColorConstants.Black
        finally:
            QGuiApplication.restoreOverrideCursor()
        return avgColor


    def computeRGBAverage(self, image):
        avgRGB = averageQImageRGB(image)
        return QColor(avgRGB[0], avgRGB[1], avgRGB[2])
