#!/usr/bin/env python3
""" This module impletemts asyncio.Task """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(delay):
    """ returns a <asyncio.Task> object from wait_random """
    task = asyncio.create_task(wait_random(delay))
    return task
