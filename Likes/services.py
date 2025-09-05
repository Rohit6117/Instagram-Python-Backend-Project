from sqlalchemy.orm import Session
from fastapi import HTTPException
from Likes import schemas, models
from Posts import models as postmod
from Users import models as usermod
from datetime import datetime

'''Likes Table Logic is pending.............................................................'''
def create_like(db: Session, like: schemas.LikeData):
    # db_user=db.query(usermod.UserCreate).filter(
    #     usermod.UserCreate.user_id==like.user_id
    #     ).first()
    # if not db_user:
    #     raise HTTPException(status_code=404,detail="User Not Found")
    db_post=db.query(postmod.PostCreate).filter(
        postmod.PostCreate.post_id==like.post_id,
        postmod.PostCreate.user_id==like.user_id
        ).first()
    if not db_post:
        raise HTTPException(status_code=404,detail="Post Not Found or User Not Found.!")
    old_like = db.query(models.LikeCreate).filter(
        models.LikeCreate.post_id == like.post_id,
        models.LikeCreate.user_id == like.user_id
    ).first()
    if old_like:
        raise HTTPException(status_code=404,detail="You Are Already Liked This Post.!")
    new_like = models.LikeCreate(
        post_id=like.post_id,
        user_id=like.user_id,
        like_createdat=like.like_createdat
    )
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return new_like

def delete_post(db: Session,like_id:int):
    db_post = db.query(models.LikeCreate).filter(
        models.LikeCreate.like_id == like_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post Not Found")
    db.delete(db_post)
    db.commit()
    # return f"{db_user} UserData Deleted.!"
    return db_post