from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def get():
    with open("client.html", "r") as f:
        return HTMLResponse(content=f.read())
    
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # 1. Accept the connection
    await websocket.accept()
    try:
        while True:
            # 2. Receive text data from the client
            data = await websocket.receive_text()
            
            # 3. Send the formatted response back
            await websocket.send_text(f"Server received: {data}")
            
    except WebSocketDisconnect:
        # 4. Handle client disconnection
        print("Client disconnected")