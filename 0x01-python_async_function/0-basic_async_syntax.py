#!/usr/bin/env python3
"""
Graham S. Paul - 0-basic_async_syntax.py
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """[synopsis]

    Args:
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        float: [description] - random delay between 0 and max_delay
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
