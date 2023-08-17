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
from typing import Optional, TypeVar, Union

from numpy import (array, ndarray, flip, mean, delete, uint8)

from PySide6.QtGui import QImage


T = TypeVar('T', bound=Union[int, float])


def clamp(num: T,
          minimum: Optional[T] = None,
          maximum: Optional[T] = None) -> T:
    """
    Returns a value clamped between low and high boundaries.
    :param num: Value to clamp.
    :param minimum: The optional lower boundary.
    :param maximum: The optional upper boundary.
    :return: The value after the dead-band is applied.
    """
    if minimum is not None and num < minimum:
        return minimum
    if maximum is not None and num > maximum:
        return maximum
    return num


def get_qimage_rgb(image: QImage) -> ndarray:
    """
    Extracts the RGB value of each pixel of a QImage
    :param image: An initialized QImage
    :return: A 4D ndarray of (r,g,b) tuples grouped by columns, themselves grouped by lines.
    """
    reformatted = image.convertToFormat(QImage.Format_RGB32)
    w = reformatted.width()
    h = reformatted.height()
    bits = reformatted.constBits()
    arr = array(bits, uint8).reshape(h, w, 4)
    # Ensure the bits are ordered as ARGB regardless of endianness
    return delete(arr if byteorder == 'big' else flip(arr), 0, 2)


def average_rgb_channels(arr: ndarray) -> list[int]:
    """
    Computes the integral mean value of each individual color channel of a 4D array.
    """
    avg_lines = mean(arr[:, :, :], axis=1)
    avg_cols = mean(avg_lines, axis=0)
    return [int(avg_cols[0]), int(avg_cols[1]), int(avg_cols[2])]


def average_qimage_rgb(image: QImage) -> list[int]:
    """
    Computes the integral mean value of each color channel of a QImage.
    :param image: An initialized QImage.
    :return: An (r, g, b) int-tuple.
    """
    return average_rgb_channels(get_qimage_rgb(image))
