from pydantic import BaseModel

from typing import List
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
    id: int


class Cart(BaseModel):
    id : int
    date : datetime
    desc : str
    user_id: int | None = None
    user : FilteredUserResponse

    class Config:
        orm_mode = True

class Product(BaseModel):
    id : int
    title : str
    price : float
    description : str
    category : str

class ListProduct(BaseModel):
    posts: List[Product]


class CreateProductSchema(BaseModel):
    id : int
    title : str
    price : float
    description : str
    category : str

class CreateCartSchema(BaseModel):
    id : int
    date : datetime = datetime.now()
    desc : str

class AddProductToCartSchema(BaseModel):
    product_id : int


