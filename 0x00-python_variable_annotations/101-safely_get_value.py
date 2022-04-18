#!/usr/bin/env python3
""" Implementing TypeVar in typing """

from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Gets valu and returns a TypeVar with no Error """
    if key in dct:
        return dct[key]
    else:
        return default
