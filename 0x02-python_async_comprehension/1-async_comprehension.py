#!/usr/bin/env python3
'''Graham S. Paul - 1-async_comprehension.py
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Develope a series of 10 digits from a 10-number generator.
    '''
    return [num async for num in async_generator()]
