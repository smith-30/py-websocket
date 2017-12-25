import asyncio
import websockets
import struct

async def hello():
    async with websockets.connect('ws://localhost:8777') as websocket:
        x = [
            0xaa,
            0x02,
            0x01,
            0x01,
            0xa, 0x0, 0x0, 0x0,
            0x01,
            0x40, 0xe2, 0x1, 0x0,
            0xa, 0x0,
            0xff, 0x35, 0x65, 0xc4, # can id
            0x04, # data length
            0x57, 0x4, 0x0, 0x0
        ]
        name = struct.pack('B'* len(x), *x)
        await websocket.send(name)
        await websocket.send(name)
        await websocket.send(name)
        print("> {}".format(name))

        # greeting = await websocket.recv()
        # print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())