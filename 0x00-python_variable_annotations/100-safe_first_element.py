#!/usr/bin/env python3
"""
This module contains the function safe_first_element that takes a list lst of
any type as argument and returns the first element of the list if it exists,
otherwise None.
"""


from typing import Any, List, Union


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """
    This function takes a list lst of any type as argument and
      returns the first element of the list if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
