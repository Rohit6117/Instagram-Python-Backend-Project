from sqlalchemy import Column,Integer,Float,String
from sqlalchemy.orm import declarative_base,relationship
from database.db import Base


class UserCreate(Base): 
    __tablename__='Userss'
    user_id=Column(Integer,primary_key=True)
    user_name=Column(String,nullable=False,unique=True)
    user_email=Column(String,nullable=False,unique=True)
    user_fullname=Column(String,nullable=False)
    user_bio=Column(String)
    user_createdat=Column(String)
    user_password=Column(String)
    
    posts=relationship("PostCreate",back_populates='user1')
    comments=relationship("CommentCreate",back_populates='user3')
    likes=relationship("LikeCreate",back_populates="user2")
    