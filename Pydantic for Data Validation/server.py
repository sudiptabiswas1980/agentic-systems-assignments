from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class UserRegister(BaseModel):
    # min_length ensures the string isn't too short
    username: str = Field(..., min_length=5, description="Username must be at least 5 characters")
    
    # EmailStr automatically validates the format (e.g., must have @ and a domain)
    email: EmailStr
    
    # ge stands for "greater than or equal to"
    age: int = Field(..., ge=18, description="User must be at least 18 years old")

@app.post("/register")
async def register_user(user: UserRegister):
    # If the data reaches here, it has already been validated
    return {"message": "User registered successfully", "user": user}