#!/usr/bin/env python3
""" this is async time calculator """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ calls task_wait_random n times and returns the list of time """
    time_list: List[float] = []
    for i in asyncio.as_completed([task_wait_random(max_delay)
                                   for _ in range(n)]):
        res = await i
        time_list.append(res)
    return time_list
