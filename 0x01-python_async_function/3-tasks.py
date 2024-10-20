#!/usr/bin/env python3
"""
This module contains a function that creates and returns an asyncio.Task
for the wait_random coroutine imported from the 0-basic_async_syntax module.
"""

import asyncio
from random import uniform

# Import the wait_random function from the 0-basic_async_syntax module
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum value for the random delay.

    Returns:
        asyncio.Task: The asyncio.Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
