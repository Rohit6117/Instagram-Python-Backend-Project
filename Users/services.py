from sqlalchemy.orm import Session
from fastapi import HTTPException
from Users import schemas, models
import auth
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime
from Posts import models as postmod
from Likes import models as likemod
from Comments import models as commentmod
import captcha

def create_user(db: Session,captchaa:schemas.CaptchaSchema, user: schemas.UserData):

    captcha.validate_captcha(captchaa.captcha_text)
    
    db_user = db.query(models.UserCreate).filter(models.UserCreate.user_email == user.user_email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw=auth.hash_password(user.user_password)
    new_user = models.UserCreate(
        user_name=user.user_name,
        user_email=user.user_email,
        user_fullname=user.user_fullname,
        user_phone=user.user_phone,
        user_gender=user.user_gender,
        user_dob=str(user.user_dob),
        user_bio=user.user_bio,
        user_password=hashed_pw,
        user_created_dt=str(datetime.utcnow())
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # return f"{db_user} UserData Add Successfully.!" 
    return new_user

def login(form_data: OAuth2PasswordRequestForm, db: Session):
    user = db.query(models.UserCreate).filter(models.UserCreate.user_email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.user_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = auth.create_access_token(data={"sub": user.user_email})
    return {"access_token": token, "token_type": "bearer"}

def update_user(token:str,db: Session, user: schemas.UserUpdatedData):
    email = auth.verify_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")
    db_user = db.query(models.UserCreate).filter(
        models.UserCreate.user_email==email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User Not Found.!")

    db_user.user_name = user.user_name
    db_user.user_email = user.user_email
    db_user.user_fullname=user.user_fullname
    db_user.user_bio=user.user_bio
    # db_user.user_createdat=user.user_updatedat
    db_user.user_created_dt=datetime.utcnow()
    db.commit()
    db.refresh(db_user) 
    # return f"{db_user} UserData Update Successfully.!" 
    # return db_user
    return schemas.UserUpdatedResponse(
        user_name=db_user.user_name,
        user_email=db_user.user_email,
        user_fullname=db_user.user_fullname,
        user_bio=db_user.user_bio,
        user_updated_dt=user.user_updated_dt,

    )


def delete_user(token:str,db: Session,user_name:str,user_password:str):
    email = auth.verify_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    db_user=db.query(models.UserCreate).filter(
        models.UserCreate.user_email==email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User Not Found.!")
    
    user = db.query(models.UserCreate).filter(
        models.UserCreate.user_name == user_name).first()
    user_pass= auth.verify_password(user_password,user.user_password)
    if not user_pass:
        raise HTTPException(status_code=404, detail="Incorrect Password.!")
    db.delete(db_user)
    db.commit()
    # return f"{db_user} UserData Deleted.!"
    return db_user 


from sqlalchemy import func
def see_all_userdata(token: str, db: Session):
    email = auth.verify_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Find logged-in user
    user = db.query(models.UserCreate).filter(models.UserCreate.user_email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # like_count=

    result = (
        db.query(
            postmod.PostCreate.post_id,
            postmod.PostCreate.post_url,
            postmod.PostCreate.post_caption,
            func.count(likemod.LikeCreate.like_id).label("like_count"),
            func.group_concat(commentmod.CommentCreate.comment_text, ' | ').label("comments")
        )
        .join(models.UserCreate, models.UserCreate.user_id == postmod.PostCreate.user_id)
        .outerjoin(likemod.LikeCreate, postmod.PostCreate.post_id == likemod.LikeCreate.post_id)
        .outerjoin(commentmod.CommentCreate, postmod.PostCreate.post_id == commentmod.CommentCreate.post_id)
        .filter(models.UserCreate.user_id == user.user_id)
        .group_by(
            postmod.PostCreate.post_id,
            postmod.PostCreate.post_url,
            postmod.PostCreate.post_caption
        )
        .all()
    )

    posts = [
        {
            "post_id": r[0],
            "post_url": r[1],
            "post_caption": r[2],
            "like_count": r[3],
            "comments": r[4] if r[4] else ""
        }
        for r in result
    ]

    return {
        "user_id": user.user_id,
        "user_name": user.user_name,
        "posts": posts
    }
