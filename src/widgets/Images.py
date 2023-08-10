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


class ImageRoiSelector(QWidget):
    """
    Widget that can draw a rectangle on an image.
    """
    def __init__(self, bg: QImage, screen: QScreen):
        super().__init__()
        # UI setup
        self.setScreen(screen)
        self.move(screen.geometry().x(), screen.geometry().y())
        self.setWindowTitle("cs3 — Region Selector")
        # Class members definition
        self.bg = bg
        self.roi = None
        self.penOuter = QPen()
        self.penInner = QPen()
        # Class members setup
        self.penOuter.setColor(QColor(0, 0, 0))
        self.penOuter.setWidth(4)
        self.penInner.setColor(QColor(255, 255, 255))
        self.penInner.setStyle(Qt.DashDotLine)
        self.penInner.setWidth(2)

    # QT Override
    def paintEvent(self, event: QPaintEvent):
        """
        Draws the outline of the region of interest on the widget.
        """
        qp = QPainter()
        qp.begin(self)
        try:
            if self.bg is not None:
                qp.drawImage(0, 0, self.bg)
            if self.roi is not None:
                qp.setPen(self.penOuter)
                qp.drawRect(self.roi)
                qp.setPen(self.penInner)
                qp.drawRect(self.roi)
        finally:
            qp.end()

    def update_roi(self, roi: QRect):
        """
        Update the geometry of the region of interest.
        """
        self.roi = roi
        self.update()
