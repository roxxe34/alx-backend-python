#!/usr/bin/env python3
"""
task 11 advanced
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Retrieves a value from a dict using a key.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
