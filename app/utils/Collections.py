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


from typing import Iterable, Optional, Any

from app.utils.Maths import clamp


class CollectionFormatter:
    """
    Formatter to stringify collections with additional start, separator and end symbol(s).
    """
    def __init__(self, start: str = '(', sep: str = ',', end: str = ')'):
        self.start = self.safe_string_format(start)
        self.sep = self.safe_string_format(sep)
        self.end = self.safe_string_format(end)

    def set_start(self, start: str) -> None:
        """
        Sets the starting symbol(s).
        """
        self.start = self.safe_string_format(start)

    def set_sep(self, sep: str) -> None:
        """
        Sets the item separator symbol(s).
        """
        self.sep = self.safe_string_format(sep)

    def set_end(self, end: str) -> None:
        """
        Sets the ending symbol(s)
        """
        self.end = self.safe_string_format(end)

    def format(self, arr: Iterable) -> str:
        """
        Displays all elements of the collection in a string using the start, separator and end symbols.
        """
        return f'{self.start}{self.sep.join(str(x) for x in arr)}{self.end}'

    @staticmethod
    def safe_string_format(text: Optional[str]) -> str:
        """
        Converts None string into empty string.
        """
        return '' if text is None else text


class ActiveList(list):
    """
    Stateful list that keep track of a single active index at the time.
    """
    def __init__(self, *args):
        super().__init__(args)
        self.activeIndex = None

    def append(self, val) -> None:
        """
        Adds an entry to the list and sets the active index to its end.
        """
        super().append(val)
        self.activeIndex = len(self) - 1

    def get_active(self) -> Optional[Any]:
        """
        Gets the element under the active index.
        :return: The element under the active index if defined, None otherwise.
        """
        return self[self.activeIndex] if self.activeIndex is not None else None

    def move_to_previous(self) -> None:
        """
        Moves the active index to the previous element, up to the first element.
        """
        if self.activeIndex is not None:
            self.activeIndex = clamp(self.activeIndex - 1, minimum=0)

    def move_to_next(self) -> None:
        """
        Moves the active index to the next element, up to the last element.
        """
        if self.activeIndex is not None:
            self.activeIndex = clamp(self.activeIndex + 1, maximum=len(self) - 1)

    def at_start(self) -> bool:
        """
        Checks if the active index is at first element of the list.
        """
        return self.activeIndex is None or self.activeIndex == 0

    def at_end(self) -> bool:
        """
        Checks if the active index is at the end of the list.
        """
        return self.activeIndex is None or self.activeIndex == len(self) - 1

    def empty(self) -> bool:
        """
        Checks if there is no element in the list.
        """
        return len(self) == 0
