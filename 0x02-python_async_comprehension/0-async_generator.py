#!/usr/bin/env python3
""" This module uses async comprehension """

import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """ This function uses async generator
    to generate numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield float(random.randint(0, 10))
