# client_transport.py
# pip install websockets
# Do not modify this file. 
# Perform your client-side testing by modifying test_client.py after running the websocket_erver.

import asyncio
import websockets
import json


class GameClient:

    def __init__(self, uri="ws://localhost:8765"):
        self.uri = uri
        self.websocket = None
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    # ------------------------
    # INTERNAL ASYNC METHODS
    # ------------------------

    async def _connect(self):
        self.websocket = await websockets.connect(self.uri)

    async def _send(self, data):
        await self.websocket.send(json.dumps(data))

    async def _receive(self):
        response = await self.websocket.recv()
        return json.loads(response)

    async def _close(self):
        await self.websocket.close()

    # ------------------------
    # PUBLIC SYNC INTERFACE
    # ------------------------

    def connect(self):
        self.loop.run_until_complete(self._connect())

    def send_action(self, action, **kwargs):
        message = {"action": action}
        message.update(kwargs)
        self.loop.run_until_complete(self._send(message))
        return self.loop.run_until_complete(self._receive())

    def close(self):
        self.loop.run_until_complete(self._close())
        self.loop.close()