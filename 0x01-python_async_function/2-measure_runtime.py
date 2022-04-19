#!/usr/bin/env python3
""" This module uses the time module to calculate elapse time """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n, max_delay):
    """ calculates the runtime """
    start = s = time.perf_counter()
    await wait_n(n, max_delay)
    elapsed = time.perf_counter() - start

    return float(elapsed)
