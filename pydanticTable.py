
from pydantic  import BaseModel
# chat model request  
class chatRquest  (BaseModel):
    id : int 
    message : str

# chat model response  
class chatResponse (BaseModel):
    id : int 
    message : str


# fot users (signup/) 
class UserCreate(BaseModel):
    username: str
    password: str


# login
class UserResponse(BaseModel):
    id: int
    username: str

   