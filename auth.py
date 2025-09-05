from passlib.context  import CryptContext
from jose import JWTError,jwt
from datetime import datetime,timedelta


SECRET_KEY="mysecret"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MIN=30

pwt_context=CryptContext(schemes=['bcrypt'],deprecated="auto")

def hash_password(password:str):
    return pwt_context.hash(password)

def verify_password(plain,hashed):
    return pwt_context.verify(plain,hashed)

def create_access_token(data:dict,expires_delta: timedelta | None = None):
    to_encode=data.copy()
    expire=datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MIN))
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

def verify_token(token:str):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload.get('sub')
    except JWTError:
        return None