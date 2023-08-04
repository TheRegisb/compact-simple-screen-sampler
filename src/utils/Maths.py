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

from sys import byteorder

from numpy import (array, ndarray, flip, mean, delete, uint8)

from PySide6.QtGui import QImage


def clamp(num, minimum=None, maximum=None):
    if minimum is not None and num < minimum:
            return minimum
    if maximum is not None and num > maximum:
        return maximum
    return num


def getQImageRGB(image: QImage) -> ndarray:
    """
    Extract the RGB value of each pixels as a 4D array of
    (r,g,b) tuples grouped by columns, themselves grouped by lines.
    """
    reformatted = image.convertToFormat(QImage.Format_RGB32)
    w = reformatted.width()
    h = reformatted.height()
    bits = reformatted.constBits()
    arr = array(bits, uint8).reshape(h, w, 4)
    # Ensure the bits are ordered as ARGB regardless of endianness
    return delete(arr if byteorder == 'big' else flip(arr) , 0, 2)


def averageRGBChannels(arr: ndarray) -> list[int]:
    """
    Compute the integral mean value of each individual
    color channel of a 4D array. 
    """
    avgLines = mean(arr[:, :, :], axis=1)
    avgCol = mean(avgLines, axis=0)
    return [int(avgCol[0]), int(avgCol[1]), int(avgCol[2])]


def averageQImageRGB(image: QImage) -> list[int]:
    return averageRGBChannels(getQImageRGB(image))
