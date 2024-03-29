#!/usr/bin/env python3
"""Graham S. Paul - 3.tasks.py"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """[synopsis]

    Args:
        max_delay (int): [explanation]

    Returns:
        asyncio.Task: [explanation]
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
