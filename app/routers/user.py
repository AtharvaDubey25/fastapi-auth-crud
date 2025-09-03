from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from .. import models,schemas,database
from ..hashing import Hash

router = APIRouter(tags=['/Users'],prefix='/user')

@router.post('/',response_model=schemas.User)
async def create_user(request:schemas.UserCreate,db:Session = Depends(database.get_db)):
    hashed_password=Hash.bcrypt(request.password)
    new_user=models.User(
        username=request.username
    ,   email=request.email,
    password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}",response_model=schemas.User)
async def get_user(id:int , db : Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    return user
