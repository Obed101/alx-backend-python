#!/usr/bin/env python3
""" Fixing unknown annotations """
from typing import Any, Sequence, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns an empty list or none"""
    if lst:
        return lst[0]
    else:
        return None
