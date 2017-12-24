import asyncio
import websockets
import struct

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        name = struct.pack('BBB', 0xaa, 0xcd, 0xaa)
        await websocket.send(name)
        await websocket.send(name)
        await websocket.send(name)
        print("> {}".format(name))

        # greeting = await websocket.recv()
        # print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())