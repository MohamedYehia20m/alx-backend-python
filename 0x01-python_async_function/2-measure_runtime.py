#!/usr/bin/env python3
"""
This module provides a function to measure the execution time of
the wait_n function and return the average time per call.
"""

import time
import asyncio

# Import the wait_n function from the module where it is defined
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n and return the average time
    per call.

    Args:
        n (int): The number of times wait_n will be executed.
        max_delay (int): The maximum delay for each call.

    Returns:
        float: The average execution time per call.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start_time

    return elapsed / n
