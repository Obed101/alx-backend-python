#!/usr/bin/env python3
"""Annotation of list of floats"""
import typing


def sum_list(input_list: typing.list[float]) -> float:
    """Adds everything in input_list"""
    a: float = 0.00
    for i in input_list:
        if type(i) == float:
            a += i
    return a
