import random,string
from datetime import datetime,timedelta
from fastapi import HTTPException
from sqlalchemy.orm import Session


captcha_store={}


def generate_captcha_text(length=7):
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(length))

# def create_captcha_text():
#     text= generate_captcha_text()
#     captcha_store[text]=datetime.utcnow + timedelta(minutes=5)
#     return {"Captcha Text": text}
def create_captcha_text():
    text = generate_captcha_text()
    # Store captcha with 5 min expiry
    captcha_store[text] = datetime.utcnow() + timedelta(minutes=5)
    return text   
    
def validate_captcha(captcha_text: str):
    if captcha_text not in captcha_store:
        raise HTTPException(status_code=400, detail="Invalid or expired captcha")

    # Check expiry
    expiry = captcha_store[captcha_text]
    if datetime.utcnow() > expiry:
        del captcha_store[captcha_text]
        raise HTTPException(status_code=400, detail="Captcha expired")

    # Remove after use (one-time)
    del captcha_store[captcha_text]
    return True

