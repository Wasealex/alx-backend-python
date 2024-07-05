#!/usr/bin/env python3
"""
This module contains the function element_length that takes a list lst of
strings as argument and returns a list of tuples where each tuple
contains a string and its corresponding length.
"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    This function takes a list lst of strings as argument and returns a list of
    tuples where each tuple contains a string and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
