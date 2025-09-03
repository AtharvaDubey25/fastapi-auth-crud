from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()  # loads environment variable from .env file

SQLALCHEMY_DATABASE_URL=os.getenv("DATABASE_URL")  # bring me the env variable named database url from .env

engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})  # create an engine that connect the code with the database url

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine) # make a session object that makes a session everytime it is called and use the engine that contains the database url 

def get_db():
    db = SessionLocal() # SessionObject

    try:
        yield db # runs when db:Session = Depends(get_db) basically get_db is a dependency and db is dependent on it 
    finally:
        db.close() # whether or not the above call gives error or not close db to stop leaks.

Base=declarative_base()  # declarative base instance every class in models inherits from this so that code can find which class needs to be a table in database
