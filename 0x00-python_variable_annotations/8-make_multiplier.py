#!/usr/bin/env python3
"""This method manipulates complex mixture of types"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ uses lambda to multiply
    a float by multiplier
    """
    return lambda x: x * multiplier
