from sqlalchemy import Column,Integer,String,ForeignKey
from .database import Base

class User(Base):   #inheritingfrom Base means this class will be a table in db
    __tablename__ = "users"  # database table name

    id=Column(Integer,primary_key=True,index=True)  # this is the id for evry user (index=True so we can search individual user in O(1) time)
    username=Column(String)
    email=Column(String)
    password=Column(String)


