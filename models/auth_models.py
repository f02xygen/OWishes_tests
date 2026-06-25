from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID

class UserRegisterRequestModel(BaseModel):
    email: EmailStr
    name: str
    password: str

class UserLoginRequestModel(BaseModel):
    username: EmailStr
    password: str

class UserInfoResponseModel(BaseModel):
    id: UUID
    email: EmailStr
    name: str
    created_at: datetime