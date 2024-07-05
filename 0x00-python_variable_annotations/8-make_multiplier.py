#!/usr/bin/env python3
"""
This module contains the function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float multiplier as argument and returns a function
        that multiplies a float by multiplier.
        """
    def multiply(num: float) -> float:
        """
        This function multiplies a float by multiplier.
        """
        return num * multiplier
    return multiply
