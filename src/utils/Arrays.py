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


from typing import Iterable, Optional
from utils.Maths import clamp

class ArrayFormatter():
    def __init__(self, start: str='(', sep: str=',', end: str=')'):
        self.start = self.safeStringFormat(start)
        self.sep = self.safeStringFormat(sep)
        self.end = self.safeStringFormat(end)

    def setStart(self, start: str):
        self.start = self.safeStringFormat(start)

    def setSep(self, sep: str):
        self.sep = self.safeStringFormat(sep)

    def setEnd(self, end: str):
        self.end = self.safeStringFormat(end)

    def format(self, arr: Iterable) -> str:
        return f'{self.start}{self.sep.join(str(x) for x in arr) }{self.end}'

    @staticmethod
    def safeStringFormat(str: Optional[str]) -> str:
        return '' if str is None else str


class ActiveArray(list):
    def __init__(self, *args):
        self.activeIndex = None


    def append(self, val) -> None:
        super().append(val)
        self.activeIndex = len(self) - 1


    def getActive(self):
        return self[self.activeIndex] if self.activeIndex is not None else None


    def moveToPrevious(self):
        if self.activeIndex is not None:
            self.activeIndex = clamp(self.activeIndex - 1, minimum=0)

    def moveToNext(self):
        if self.activeIndex is not None:
            self.activeIndex = clamp(self.activeIndex + 1, maximum=len(self) - 1)


    def atStart(self) -> bool:
        return self.activeIndex is None or self.activeIndex == 0


    def atEnd(self) -> bool:
        return self.activeIndex is None or self.activeIndex == len(self) - 1


    def empty(self) -> bool:
        return len(self) == 0
