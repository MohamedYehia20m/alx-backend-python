#!/usr/bin/env python3
"""
This module provides an asynchronous function to execute multiple tasks
that wait for random delays and return a sorted list of these delays.
"""

import asyncio
from typing import List

# Import task_wait_random from the module where it is defined
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute task_wait_random 'n' times with a maximum delay of 'max_delay'
    and return a list of delays sorted in ascending order.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum value for each random delay.

    Returns:
        List[float]: A sorted list of delays.
    """
    delays = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        # Insert delay in sorted order
        if not delays:  # If the list is empty
            delays.append(delay)
        else:
            # Find the correct position to insert the new delay
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    break
            else:
                # If the new delay is greater than all existing ones, append it
                delays.append(delay)
    return delays
