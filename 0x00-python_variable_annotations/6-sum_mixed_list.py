#!/usr/bin/env python3
""" This module adds different annotated items"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function returns addition of ints and floats"""
    return float(sum(mxd_lst))
