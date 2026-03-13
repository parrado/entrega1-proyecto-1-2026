# websocket_server.py
# pip install websockets
# Do not modify this file. Implement all logic in game_engine.py and server_adapter.py.

import asyncio
import websockets
import json
from server_adapter import handle_request

connected_players = {}  # websocket -> player_id


async def handler(websocket):
    async for message in websocket:
        try:
            request = json.loads(message)
           
            # Inject player_id automatically to request if websocket is already associated with a player
            if websocket in connected_players:
                request["player_id"] = connected_players[websocket]

            # Route request to server adapter and get response
            response = handle_request(request)

            # Save player_id after join
            if request.get("action") == "join":
                if response.get("status") == "ok":
                    connected_players[websocket] = response.get("player_id")

            # Send response back to client
            await websocket.send(json.dumps(response))

        except Exception as e:
            error_response = {
                "status": "error",
                "message": str(e)
            }
            await websocket.send(json.dumps(error_response))


async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    print("WebSocket server for Parchis started on ws://localhost:8765")

    asyncio.run(main())
