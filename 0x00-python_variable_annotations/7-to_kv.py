#!/usr/bin/env python3
'''Task 7's module.
'''
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns a tuple.
    '''
    return (k, float(v ** 2))
