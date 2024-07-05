#!/usr/bin/env python3
"""
This module contains the function sum_mixed_list that takes a list mxd_lst
of integers and floats as argument and returns their sum as a float.
"""


from typing import List


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    """
    This function takes a list mxd_lst of integers and floats as argument and
    returns their sum as a float.
    """
    return sum(mxd_lst)
