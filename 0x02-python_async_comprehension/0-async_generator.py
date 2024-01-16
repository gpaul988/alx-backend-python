#!/usr/bin/env python3
'''Graham S. Paul - 0.async_generator.py
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Develope a series of 10 digits.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
