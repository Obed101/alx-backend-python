#!/usr/bin/env python3
""" This module uses async comprehension """

import asyncio
import random
from typing import Iterator

async def async_generator() -> Iterator[int]:
    """ This function uses async comprehension
    to generate numbers
    """
    number = random.randint(0, 10)
    for _ in range(10):
        asyncio.wait(1)
        yield random.randint(0, 10)
