#!/usr/bin/env python3
"""This method manipulates complex mixture of types"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns manipulated complex types"""
    return tuple([k, v ** 2])
