#!/usr/bin/env python3
"""
Graham S. Paul - 1-concurrent_coroutines.py
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """Detail: [description] - list of all the delays (float values)"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
