#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio,threading

async def hello():
    print('Hello World1! (%s)' % threading.currentThread())
    await asyncio.sleep(2)
    print('Hello World2! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
