from pydantic import BaseModel

class User(BaseModel):  #to return responses
    id:int
    username:str
    email:str
    
    class Config:
         from_attribute=True


class UserCreate(BaseModel):  # in creation moment
    username:str
    email:str
    password:str

class User_in_db(User): # storing the data in the database
    password:str

class Login(BaseModel):
    email: str
    password: str