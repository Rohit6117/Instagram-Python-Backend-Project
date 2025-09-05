from pydantic import BaseModel ,EmailStr
from datetime import datetime

class UserData(BaseModel):
    user_name:str
    user_email:EmailStr
    user_fullname:str
    user_bio:str
    user_createdat:datetime
    user_password:str

class CaptchaSchema(BaseModel):
    captcha_text: str


class UserUpdatedData(BaseModel):
    user_name:str
    user_email:EmailStr
    user_fullname:str
    user_bio:str
    user_updatedat:datetime #|None =None

class UserUpdatedResponse(UserUpdatedData):
    pass
    
class UserResponse(UserData):
    user_id: int
    
    class Config:
        from_attributes =True
        
class Token(BaseModel):
    access_token:str
    token_type:str
   

from pydantic import BaseModel
from typing import Optional, List

class PostWithMeta(BaseModel):
    post_id: int
    post_url: str
    post_caption: str
    like_count: int
    comments: Optional[str]  # concatenated comments

class UserWithPosts(BaseModel):
    user_id: int
    user_name: str
    posts: List[PostWithMeta]
