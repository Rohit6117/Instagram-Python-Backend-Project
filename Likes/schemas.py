from pydantic import BaseModel
from datetime import datetime

class LikeData(BaseModel):
    post_id:int
    user_id:int
    like_createdat:datetime
    
class LikeResponse(LikeData):
    like_id:int
    
    class Config:
        from_attributes=True
    