from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from datetime import timedelta
from .. import schemas,database,models,token
from ..hashing import Hash
from dotenv import load_dotenv
import os

load_dotenv() 


router = APIRouter(prefix='/auth',tags=['Authentication'])


ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


@router.post('/login')
def login(request:schemas.Login , db : Session = Depends(database.get_db)):
    #find the user by email 
    user = db.query(models.User).filter(models.User.email==request.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'user with the email ID {request.email} not found try with different email ID'
        )
    
    if not Hash.verify(request.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='incorrect password'            
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={'sub':user.email},
        expires_delta=access_token_expires
    )

    return {
        'access_token':access_token,
        'token_type':'bearer'
    }