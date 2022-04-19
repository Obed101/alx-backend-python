#!/usr/bin/env python3
""" This is the first asyncio module """

import asyncio
import random


async def wait_random(max_delay=10):
    """ Waits for a random max_delay and returns it """
    await asyncio.sleep(random.uniform(0, max_delay))
    return float(max_delay)
