from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os


load_dotenv()

########### hashing password  
pwrd_CryptContext = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")
# user with new password 
def hash_pswr(pwr: str):
    
    return pwrd_CryptContext.hash(pwr)

#  verify password for login
def verify_pwr (*, hashed_password, plain_password ): 
    return pwrd_CryptContext.verify(plain_password, hashed_password  )

############# JWT 
# variables  
SECRET_KEY  = os.getenv("SECRET_KEY")
ALGORITHM   = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES   = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

def create_token_access(data :dict  , expires_delta: timedelta = None): 
    to_encode  = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)))
    to_encode.update({"expire": int(expire.timestamp())})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

