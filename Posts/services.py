from sqlalchemy.orm import Session
from fastapi import HTTPException
from Posts import schemas, models
from Users import models as usermod

import auth

def create_post(db: Session, post: schemas.PostData,token:str):

    email = auth.verify_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    db_user = db.query(usermod.UserCreate).filter(usermod.UserCreate.user_email == email).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="User not found")
    
    if post.user_id != db_user.user_id:
        raise HTTPException(status_code=403, detail="Incorrect User_Id Please Enter Correct User Id")
    # db_post=db.query(usermod.UserCreate).filter(
    #     usermod.UserCreate.user_id==post.user_id
    # ).first()
    # if not db_post:
    #     raise HTTPException(status_code=404, detail="User Not Found")
    new_post = models.PostCreate(
        post_url=post.post_url,
        post_caption=post.post_caption,
        user_id=post.user_id,
        post_createdat=post.post_createdat,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    # return {"message": f"Post {new_post} created successfully"}
    return new_post


def get_post(db:Session,post_id:int):
    db_post=db.query(models.PostCreate).filter(
        models.PostCreate.post_id==post_id
    ).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post Not Found")
    return db_post

    
def delete_post(post_id:int,db: Session,token:str):
    email = auth.verify_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")
    db_user = db.query(usermod.UserCreate).filter(usermod.UserCreate.user_email == email).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="User not found")
    db_post = db.query(models.PostCreate).filter(
        models.PostCreate.post_id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post Not Found")
    
    if db_post.user_id != db_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post Please Check Your post_id")
    db.delete(db_post)
    db.commit()
    # return f"{db_user} UserData Deleted.!"
    return db_post
