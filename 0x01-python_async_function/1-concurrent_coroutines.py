#!/usr/bin/env python3
""" This module uses async's concurrent coroutines """
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, delay):
    """ Uses a concurrent coroutine to call wait_random n times """
    times = []
    for wait in asyncio.as_completed([wait_random(delay) for _ in range(n)]):
        one_time = await wait
        await times.append(float(one_time))
    return times
