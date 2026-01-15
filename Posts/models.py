from sqlalchemy import Column,Integer,Float,String,ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class PostCreate(Base):
    __tablename__ = 'Postss'
    post_id = Column(Integer, primary_key=True)
    post_url = Column(String) 
    post_caption = Column(String)
    post_createdat = Column(String)
    user_id = Column(Integer, ForeignKey("Userss.user_id"))  # Must match UserCreate.__tablename__
    
    user1 = relationship("UserCreate", back_populates="posts")
    likepost = relationship("LikeCreate", back_populates='postlike')
    commentpost = relationship("CommentCreate", back_populates="postcomment")
    
    