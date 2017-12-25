import asyncio
import websockets
from websockets.extensions.permessage_deflate import ServerPerMessageDeflateFactory

async def hello(websocket, path):
    while True:
        name = await websocket.recv()
        print("< {}".format(name))

        # greeting = "Hello {}!".format(name)
        # await websocket.send(greeting)
        # print("> {}".format(greeting))

extensions = [ServerPerMessageDeflateFactory(
                    client_no_context_takeover=True,
                    server_no_context_takeover=True
                )]
    

start_server = websockets.serve(hello, 'localhost', 8777, extensions=extensions)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()