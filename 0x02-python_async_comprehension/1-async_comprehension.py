#!/usr/bin/env python3
""" This implements actual async comprehension """

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Uses Async Generator to create Async Comprehension """
    return [i async for i in async_generator()]
