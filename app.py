from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import time

app = FastAPI()

@app.websocket("/test")
async def test(websocket: WebSocket):
    await websocket.accept()
    await asyncio.sleep(1000)
