from fastapi import APIRouter, Depends
from Comments import schemas, services
from sqlalchemy.orm import Session
from database.db import get_db
from Users.routers import oauth2_scheme

commentrouter=APIRouter()
@commentrouter.post("/Comment", response_model=schemas.CommentResponse)
def create_comments(comment: schemas.CommentData, db: Session = Depends(get_db)):
    return services.create_comment(db, comment)

@commentrouter.delete("/CommentDelete",response_model=schemas.CommentResponse)
def delete_comments(comment_id:int,token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    return services.delete_comment(db,comment_id,token)