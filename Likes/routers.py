from fastapi import APIRouter, Depends
from Likes import schemas, services
from sqlalchemy.orm import Session
from database.db import get_db

likerouter=APIRouter()
@likerouter.post("/Likes", response_model=schemas.LikeResponse)
def create_posts(like: schemas.LikeData, db: Session = Depends(get_db)):
    return services.create_like(db, like)

@likerouter.delete("/DeleteLike",response_model=schemas.LikeResponse)
def delete_posts(like_id:int,db:Session=Depends(get_db)):
    return services.delete_post(db,like_id)