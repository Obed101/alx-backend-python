#!/usr/bin/env python3
""" This implements actual async comprehension """

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Uses Async Generator to create Async Comprehension """
    numbers = [i async for i in async_generator()]
    return numbers
