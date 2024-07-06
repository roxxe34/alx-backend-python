#!/usr/bin/env python3

'''Task 0's module.
'''
import random
import asyncio
async def wait_random(max_delay: int=10) -> float:
    '''Waits for a random number of seconds.
    '''
    r = random.random() * max_delay
    await asyncio.sleep(r)
    return r