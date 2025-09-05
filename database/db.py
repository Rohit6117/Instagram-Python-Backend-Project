from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

Base=declarative_base()

DATABASE_URL='sqlite:///Instagram.db'
engine=create_engine(DATABASE_URL,connect_args={'check_same_thread':False})
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
    
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# models1.Base.metadata.create_all(bind=engine)
# models2.Base.metadata.create_all(bind=engine)

# class Base(declarative_base):
#     pass