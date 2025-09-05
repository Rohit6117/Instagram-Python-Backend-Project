from sqlalchemy.orm import Session
from fastapi import HTTPException
from Comments import schemas, models
from Posts import models as postmod
from Users import models as usermod
import auth

def create_comment(db:Session,comment:schemas.CommentData):
    db_user=db.query(postmod.PostCreate).filter(
        postmod.PostCreate.user_id==comment.user_id,
        postmod.PostCreate.post_id==comment.post_id
        ).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="User Not Found or post not Found")
    # db_post=db.query(postmod.PostCreate).filter(
    #     postmod.PostCreate.post_id==comment.post_id
    #     ).first()
    # if not db_post:
    #     raise HTTPException(status_code=404,detail="Post Not Found")
    new_comment = models.CommentCreate(
        post_id=comment.post_id,
        user_id=comment.user_id,
        comment_text=comment.comment_text,
        comment_createdat=comment.comment_createdat,
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def delete_comment(db: Session,comment_id:int,token:str):
    email = auth.verify_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    db_user = db.query(usermod.UserCreate).filter(usermod.UserCreate.user_email == email).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="User not found")
    
    db_comment = db.query(models.CommentCreate).filter(             
        models.CommentCreate.comment_id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment Not Found")
    
    if db_user.user_id != db_comment.user_id:
        raise HTTPException(status_code=404,detail="You Can't Delete this comment.!")
    db.delete(db_comment)
    db.commit()
    # return f"{db_user} UserData Deleted.!"
    return db_comment
    