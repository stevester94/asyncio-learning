#! /usr/bin/env python3
import asyncio

"""
This one really demonstrates how this shit is not multithreaded. They are perfectly interleaved which shows how the event loop is handing off at 
each call of await
"""

async def spinner( arg ):
    for _ in range(10):
        print( arg )
        await asyncio.sleep(0.1)



async def top():
    t1 = asyncio.create_task( spinner("kek") )
    t2 = asyncio.create_task( spinner("lel") )

    await t1, t2


asyncio.run(
    top()
)