#!/usr/bin/env python3
"""Task 1's module.
"""
from typing import List
from asyncio import gather

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait-n function
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await gather(*tasks)
    return sorted(results)
