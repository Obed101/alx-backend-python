#!/usr/bin/env python3
""" This module uses the time module to calculate elapse time """
import asyncio
import time
from typing import List

wait_n: List[float] = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ calculates the runtime """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed: float = time.perf_counter() - start
    return float(elapsed / n)
