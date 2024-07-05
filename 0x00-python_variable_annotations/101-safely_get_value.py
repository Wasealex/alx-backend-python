#!/usr/bin/env python3
"""
This module contains the function safely_get_value that takes a dictionary dct
and a key key as arguments and returns the value of the key if it exists,
otherwise None.
"""


from typing import Dict, Any, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Dict[Any, T], key: Any, default: T = None) -> T:
    """
    This function takes a dictionary dct and a key key as arguments and
        returns the value of the key if it exists, otherwise None.
        """
    if key in dct:
        return dct[key]
    else:
        return default
