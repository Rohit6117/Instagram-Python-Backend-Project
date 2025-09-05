from sqlalchemy import Column,Integer,Float,String,ForeignKey
from sqlalchemy.orm import declarative_base,relationship
from database.db import Base

class CommentCreate(Base):
    __tablename__='Commentss'
    comment_id=Column(Integer,primary_key=True)
    comment_text=Column(String)
    comment_createdat=Column(String)
    post_id=Column(Integer,ForeignKey("Postss.post_id"))
    user_id=Column(Integer,ForeignKey("Userss.user_id"))
    
    user3=relationship("UserCreate",back_populates="comments")
    postcomment=relationship("PostCreate",back_populates="commentpost")
    