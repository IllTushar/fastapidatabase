from pydantic import BaseModel
from typing import Optional
##This model is used for dataValidations 
class Product(BaseModel):
    name:str
    decription:str
    price:int

class Filter_Details(BaseModel):
    name:str
    decription:str
    class Config:
        orm_mode=True

class Seller(BaseModel):
    name:str
    email:str
    password:str

class DisplaySeller(BaseModel):
    name :str
    email:str
    seller :Seller
    class Config:
        orm_mode =True


class Display(BaseModel):
    name:str
    email:str
    class Config:
        orm_mode = True
        
class Login(BaseModel):
    name:str
    password:str

class Token(BaseModel):
    access_token:str
    token_ty:str

class Token_Data(BaseModel):
    name:Optional[str]
