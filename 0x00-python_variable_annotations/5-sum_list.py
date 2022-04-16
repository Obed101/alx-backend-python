#!/usr/bin/env python3
"""Annotation of list of floats"""


def sum_list(input_list: list) -> float:
    """Adds everything in input_list"""
    a: float = 0.00
    for i in input_list:
        if type(i) == float:
            a += i
    return a
