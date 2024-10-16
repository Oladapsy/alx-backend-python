#!/usr/bin/env python3
""" async coroutine """
import asyncio
import random


async def wait_random(max_delay=10):
    """ a fuction that returns after the delay"""
    ret = random.uniform(0, max_delay)
    await asyncio.sleep(ret)
    return ret
