import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

# 1. Custom 404 Exception Handler
@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"message": "The requested resource was not found"},
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# 2. Middleware for Logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Logs before processing
    print(f"--- Before Request: {request.method} {request.url.path} ---")
    
    start_time = time.time()
    
    # Process the request
    response = await call_next(request)
    
    # Logs after processing
    process_time = time.time() - start_time
    print(f"--- After Response: Processed in {process_time:.4f}s ---")
    
    return response

# 3. Simple API Endpoint
@app.get("/hello")
async def say_hello():
    return {"message": "Hello, Welcome to FastAPI!"}