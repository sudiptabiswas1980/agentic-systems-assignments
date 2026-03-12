from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/search")
async def search_user(name: Optional[str] = None, age: Optional[int] = None):
    # FastAPI automatically parses query parameters from the URL
    # and converts 'age' to an integer based on the type hint.
    return {"name": name, "age": age}