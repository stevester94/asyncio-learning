#! /usr/bin/env python3
import asyncio

async def t():
    print( "lel" )


async def top():
    print( "Begin" )
    task = asyncio.create_task( t() )
    print( "Done" )



"""
We'll get 
Begin
Done
lel
"""
asyncio.run( top() )




async def top():
    print( "Begin" )
    task = asyncio.create_task( t() )
    await task
    print( "Done" )

"""
We'll get 
Begin
lel
Done
"""
asyncio.run( top() )



# This gets a little more interesting
async def top():
    print( "Begin" )
    task = asyncio.create_task( t() )
    await asyncio.sleep( 1 )
    print( "Done" )
"""
We'll get 
Begin
lel
Done

Once we hit the await, the event loop can fire off someone else (in this case the t() task )
"""
asyncio.run( top() )