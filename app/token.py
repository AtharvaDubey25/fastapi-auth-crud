from datetime import timedelta,datetime,timezone
from jose import JWTError,jwt
from dotenv import load_dotenv
import os

load_dotenv() 

print("SECRET_KEY ->", os.getenv("SECRET_KEY"))
print("DATABASE_URL ->", os.getenv("DATABASE_URL"))

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM =os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

def create_access_token(data:dict , expires_delta : timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt