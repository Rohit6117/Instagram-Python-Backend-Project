from sqlalchemy import Column,Integer,Float,String,ForeignKey,DateTime
from sqlalchemy.orm import declarative_base,relationship
from database.db import Base

class LikeCreate(Base):
    __tablename__='Likess'
    like_id=Column(Integer,primary_key=True)
    like_createdat=Column(DateTime)
    post_id=Column(Integer,ForeignKey("Postss.post_id"))
    user_id=Column(Integer,ForeignKey("Userss.user_id"))
    
    user2=relationship("UserCreate",back_populates="likes")
    postlike=relationship("PostCreate",back_populates="likepost")
    