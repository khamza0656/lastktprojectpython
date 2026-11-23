from pydantic import BaseModel, EmailStr
from typing import Literal

class RegisterIn(BaseModel):
    email: EmailStr
    password: str
    role: Literal["user", "admin"] = "user"

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"