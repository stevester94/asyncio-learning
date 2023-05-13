#! /usr/bin/env python3
import asyncio



async def gen():
    for x in range(10):
        await asyncio.sleep(0.1)
        yield x

async def derp():
    for _ in range(20):
        print( "Derp" )
        await asyncio.sleep(0.1)

async def top():
    t = asyncio.create_task( derp() )

    g = gen()
    # You can get an awaitable for the next item to be generated
    print( await anext( g ) )

    # You can't do this!
    try:
        for x in g:
            print( x )
    except:
        pass

    # This apparently does the await as well
    # proof is we see interleaved derps
    async for x in g:
        print(x)

    # event loop will not keep firing off derp's
    # have to await for it
    await t

asyncio.run( top() )