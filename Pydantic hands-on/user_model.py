from pydantic import BaseModel, Field, EmailStr, ConfigDict

class Address(BaseModel):
    # city must be at least 3 characters
    city: str = Field(..., min_length=3)
    # pincode must be exactly 6 digits (using regex for strict validation)
    pincode: str = Field(..., min_length=6, max_length=6, pattern=r"^\d{6}$")

class User(BaseModel):
    # Assignment validation enabled via model_config
    model_config = ConfigDict(validate_assignment=True)

    user_id: int
    name: str
    email: EmailStr
    # age must be 18 or older
    age: int = Field(..., ge=18)
    address: Address
    is_premium: bool = False

# --- Verification Script ---
if __name__ == "__main__":
    try:
        user_data = {
            "user_id": 101,
            "name": "Deepak",
            "email": "deepak@example.com",
            "age": 25,
            "address": {
                "city": "Mumbai",
                "pincode": "400001"
            }
        }
        
        user = User(**user_data)
        print("User Created Successfully:")
        print(user.model_dump_json(indent=2))

        # Testing assignment validation (this will trigger an error)
        print("\nAttempting to update age to 10...")
        user.age = 10 

    except Exception as e:
        print(f"Validation Error: {e}")