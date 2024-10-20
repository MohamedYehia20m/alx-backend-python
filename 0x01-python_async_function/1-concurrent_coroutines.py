#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for multiple random
delays and returns a sorted list of these delays.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random 'n' times with a maximum delay of 'max_delay'
    and return a sorted list of delays.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum value for each random delay.

    Returns:
        List[float]: A sorted list of delays.
    """
    delays = []

    for _ in range(n):
        delay = await wait_random(max_delay)

        # Insert delay in the correct position to keep the list sorted
        inserted = False
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    return delays
