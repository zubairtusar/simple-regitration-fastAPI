from pydantic import BaseModel

class UserBase(BaseModel):
    user_name: str
    email: str
    password: str