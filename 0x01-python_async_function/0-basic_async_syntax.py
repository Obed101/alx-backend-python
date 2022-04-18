#!/usr/bin/env python3
""" This is the first asyncio module """

import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """ Waits for a random max_delay and returns it """
    await asyncio.sleep(random.randint(0, wait_random))
    return wait_random
