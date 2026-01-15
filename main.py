from fastapi import FastAPI
from Users.routers import router
from Posts.routers import postrouter
from Likes.routers import likerouter
from Comments.routers import commentrouter
from database.db import Base,engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router,tags=['Register Page'])
app.include_router(postrouter,tags=['Posts'])
app.include_router(likerouter,tags=['Likes'])
app.include_router(commentrouter,tags=['Comments'])