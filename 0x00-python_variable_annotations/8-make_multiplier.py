#!/usr/bin/env python3
'''Graham S. Paul - 8-make_multiplier.py
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Develope a multiplier function.
    '''
    return lambda x: x * multiplier
