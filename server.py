from sanic import (
    Sanic,
    response
)
from websockets.exceptions import ConnectionClosed

from room import Room


app = Sanic()
global_room = Room()


@app.route("/")
async def test(request):
        return await response.file('./static/index.html')


@app.websocket('/chat')
async def feed(request, ws):
    global_room.join(ws)
    while True:
        try:
            message = await ws.recv()
        except ConnectionClosed:
            global_room.leave(ws)
            break
        else:
            await global_room.send_message(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
