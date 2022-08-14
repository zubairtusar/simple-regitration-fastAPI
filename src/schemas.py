from pydantic import BaseModel
from fastapi import Form

class UserBase(BaseModel):
    user_name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True