#! /usr/bin/env python3

import asyncio

# async is definining a coroutine
# when you call `foo()` you actually get a coroutine object
async def foo():
    return "lel"

# Await must be in a function. We can't run this directly, gotta run in an event loop
# await foo()

# This works
print(
    asyncio.run( foo() )
)


# Standin for a long running _thing_
async def bar():
    await asyncio.sleep(1)
    return "kek"

async def combo():
    print("Start")
    ret = await bar()
    print( ret )
    print( "Finished" )


print(
    asyncio.run( combo() )
)
