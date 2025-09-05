from fastapi import APIRouter, Depends
from Posts import schemas, services
from sqlalchemy.orm import Session
from database.db import get_db

# from fastapi.security import OAuth2PasswordBearer
from Users.routers import oauth2_scheme


postrouter=APIRouter()

@postrouter.post("/Post", response_model=schemas.PostResponse)
def create_posts(post: schemas.PostData, db: Session = Depends(get_db),token:str=Depends(oauth2_scheme)):
    return services.create_post(db, post,token)

@postrouter.get("/ShowPost",response_model=schemas.PostResponse)
def create_posts(post_id:int, db: Session = Depends(get_db)):
    return services.get_post(db, post_id)

@postrouter.delete("/DeletePost",response_model=schemas.PostResponse)
def delete_posts(post_id:int,db:Session=Depends(get_db),token:str = Depends(oauth2_scheme)):
    return services.delete_post(post_id,db,token)