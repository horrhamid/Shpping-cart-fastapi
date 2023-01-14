from pydantic import BaseModel
import uuid
from datetime import datetime



class UserSchema(BaseModel):
    id : int
    username: str

    class Config:
        orm_mode = True

class CreateUserSchema(UserSchema):
    password: str

class LoginUserSchema(BaseModel):
    username: str
    password: str

class FilteredUserResponse(UserSchema):
    id: uuid.UUID


class Cart(BaseModel):
    id : uuid.UUID
    date : datetime
    desc : str
    user_id: uuid.UUID | None = None
    user : FilteredUserResponse

    class Config:
        orm_mode = True

class Products(BaseModel):
    id : uuid.UUID


    product_code : int

    title : str

    price : float
    description : str
    category : str

    
