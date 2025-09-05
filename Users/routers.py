from fastapi import APIRouter, Depends
from Users import schemas, services
from sqlalchemy.orm import Session
from database.db import get_db
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from Users.services import login
from typing import List
import captcha

router = APIRouter(prefix="/auth") 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
@router.get("/register/captcha", response_model=schemas.CaptchaSchema)
def get_captcha():
    text = captcha.create_captcha_text()
    return {"captcha_text": text}

@router.post("/user",response_model=schemas.UserResponse)
def create_users(user: schemas.UserData,captcha:schemas.CaptchaSchema, db: Session = Depends(get_db)):
    return services.create_user(db,captcha,user)

@router.post("/login", response_model=schemas.Token)
def login_users(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    return login(form_data,db)

# @router.put("/user/update/{user_id}", response_model=schemas.UserResponse)
# def update_users(user_id: int,user_password:int, user: schemas.UserData, db: Session = Depends(get_db)):
#     return services.update_user(db, user, user_id,user_password)

@router.put("/user/update/{user_id}", response_model=schemas.UserUpdatedResponse)
def update_users(user_email:str,user: schemas.UserUpdatedData, db: Session = Depends(get_db),token:str = Depends(oauth2_scheme)):
    return services.update_user(token,db, user,user_email)

@router.delete("/user/delete/{user_id}", response_model=schemas.UserResponse)
def delete_users(user_name:str,user_password:str,token:str=Depends(oauth2_scheme),db: Session = Depends(get_db)):
    return services.delete_user(token,db,user_name,user_password)

# @router.get("/user/show/{user_id}", response_model=schemas.UserResponse)
# def show_users(user_id: int,user_password:int, db: Session = Depends(get_db)):
#     return services.show_user(db, user_id,user_password)

# @router.get("/user/show/{user_id}", response_model=schemas.UserResponse)
# def show_users(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     return services.me(token,db)

@router.get("/user/alluserdata", response_model=schemas.UserWithPosts)
def show_users(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return services.see_all_userdata(token, db)
