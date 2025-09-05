from pydantic import BaseModel
from datetime import datetime
class PostData(BaseModel):
    post_url:str
    post_caption:str
    user_id:int
    post_createdat:datetime
    
class PostResponse(PostData):
    post_id:int
    
    class Config:
        from_attribute=True