import aiohttp
import aiohttp.client_ws
import asyncio

async def recv(ws: aiohttp.client_ws.ClientWebSocketResponse):
    print("Waiting for message")
    await ws.receive()

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('http://localhost:8000/test') as ws:
            # wait for the message in a separate task
            task = asyncio.create_task(recv(ws))

            # Make sure we start to wait on receiving message before close the connection
            await asyncio.sleep(0.1)

            # close the connection
            await ws.close()
            await task

            assert ws.closed
            print(f"Closed code: {ws.close_code}")


asyncio.run(main())
