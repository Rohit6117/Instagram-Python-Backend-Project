from pydantic import BaseModel
from datetime import datetime

class CommentData(BaseModel):
    comment_text:str
    post_id:int
    user_id:int
    comment_createdat:datetime
    
class CommentResponse(CommentData):
    comment_id:int
    
    
    class Config:
        from_attributes=True
        
        