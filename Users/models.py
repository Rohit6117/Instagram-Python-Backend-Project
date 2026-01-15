from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from database.db import Base

class UserCreate(Base): 
    __tablename__ = 'Userss'

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False, unique=True)
    user_email = Column(String, nullable=False, unique=True)
    user_fullname = Column(String, nullable=False)
    user_phone = Column(String)
    user_gender = Column(String)
    user_dob = Column(String)
    user_bio = Column(String)
    user_created_dt = Column(String)
    user_updated_dt = Column(String)
    user_password = Column(String, nullable=False)
    
    posts = relationship("PostCreate", back_populates='user1')
    comments = relationship("CommentCreate", back_populates='user3')
    likes = relationship("LikeCreate", back_populates="user2")
