#!/usr/bin/env python3
""" this module implements tuples of sequenses """

from typing import Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ sequencially returns a tuple """
    return [(i, len(i)) for i in lst]