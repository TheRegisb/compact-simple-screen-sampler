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

from PySide6.QtWidgets import (QWidget)
from PySide6.QtGui import (QGuiApplication, QColorConstants, QColor, QPixmap, QCursor)
from PySide6.QtCore import (Qt, Signal)

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

    def pickScreenColor(self):
        raise NotImplementedError('Error: pickScreenColor must be implemented by its subclasses')


class PixelColorPicker(ColorPicker):

    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton == Qt.LeftButton:
            try:
                self.colorSample.emit(self.pickScreenColor())
            except Exception as e:
                print('Error: Unexpected exception during picking -- releasing mouse')
                print(e)
            finally:
                self.close()
        elif event.buttons() & Qt.RightButton == Qt.RightButton:
            self.close()

    def pickScreenColor(self):
        screen = self.getActiveScreen()
        mousePos = self.getRelativeMousePosition(screen)
        image = screen.grabWindow(0).toImage()

        if image.rect().contains(mousePos):
            return QColor(image.pixel(mousePos))
        else:
            return QColorConstants.Black
            
