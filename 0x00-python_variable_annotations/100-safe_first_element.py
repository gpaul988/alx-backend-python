#!/usr/bin/env python3
'''Graham S. Paul - 100-safe_first_element.py
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Fetches the first element of a sequence if it exists.
    '''
    if lst:
        return lst[0]
    else:
        return None
