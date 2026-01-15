from pydantic import BaseModel ,EmailStr
from datetime import datetime,date
from typing import Optional, List

class UserData(BaseModel):
    user_id: Optional[int] = None
    user_name: Optional[str] = None
    user_email: Optional[EmailStr] = None
    user_fullname: Optional[str] = None
    user_phone: Optional[str] = None
    user_gender: Optional[str] = None
    user_dob: Optional[date] = None
    user_bio: Optional[str] = None
    user_created_dt: Optional[datetime] = None
    user_updated_dt: Optional[datetime] = None
    user_password: Optional[str] = None


class CaptchaSchema(BaseModel):
    captcha_text: str


class UserUpdatedData(BaseModel):
    user_name:str
    user_email:EmailStr
    user_fullname:str
    user_bio:str
    user_updated_dt:datetime #|None =None

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
