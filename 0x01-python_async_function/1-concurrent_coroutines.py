#!/usr/bin/env python3
""" This module uses async's concurrent coroutines """
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, delay: int) -> list:
    """ Uses a concurrent coroutine to spawn wait_random n times """
    tasks = [asyncio.create_task(wait_random(delay)) for _ in range(n)]
    one_time = [await wait for wait in asyncio.as_completed(tasks)]
    return one_time
