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

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (QPen, QPainter, QColor, QPaintEvent, QImage, QScreen)
from PySide6.QtCore import Qt, QRect


class SingleImage(QWidget):
    def __init__(self, bg: QImage, screen: QScreen, parent=None):
        super().__init__(parent)
        self.bg = bg
        self.setScreen(screen)
        self.move(screen.geometry().x(), screen.geometry().y())
        self.setWindowTitle('cs3 - Desktop Cover')

    # QT Override
    def paintEvent(self, event: QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        try:
            if self.bg is not None:
                qp.drawImage(0, 0, self.bg)
            self.custom_paint(qp)
        finally:
            qp.end()

    def custom_paint(self, qp: QPainter) -> None:
        """
        Custom paint procedure to be implemented by subclasses.
        :param qp: The active QPainter of this
        """
        pass


class ImageRoiSelector(SingleImage):
    """
    Widget that can draw a rectangle on an image.
    """
    def __init__(self, bg: QImage, screen: QScreen, parent=None):
        super().__init__(bg, screen, parent)
        # UI setup
        self.setWindowTitle("cs3 — Region Selector")
        # Class members definition
        self.roi = None
        self.pen_outer = QPen()
        self.pen_inner = QPen()
        # Class members setup
        self.pen_outer.setColor(QColor(0, 0, 0))
        self.pen_outer.setWidth(4)
        self.pen_inner.setColor(QColor(255, 255, 255))
        self.pen_inner.setStyle(Qt.DashDotLine)
        self.pen_inner.setWidth(2)

    def custom_paint(self, qp: QPainter) -> None:
        if self.roi is not None:
            qp.setPen(self.pen_outer)
            qp.drawRect(self.roi)
            qp.setPen(self.pen_inner)
            qp.drawRect(self.roi)

    def update_roi(self, roi: QRect):
        """
        Update the geometry of the region of interest.
        """
        self.roi = roi
        self.update()
