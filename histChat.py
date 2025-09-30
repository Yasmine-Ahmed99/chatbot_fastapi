from pydantic import BaseModel
from sqlalchemy import Column , Integer, String, DateTime
from datetime import datetime
from database import Base


class History (Base): 
    __tablename__ = "chat_history"

    #variables 
    id = Column(Integer, index = True, primary_key = True)
    user_id  = Column(Integer, nullable=False)
    user_message= Column(String , nullable=False)
    bot_massage= Column(String , nullable=False) 
    dateTime  = Column(DateTime , default=datetime.utcnow)


class User (Base): 
    __tablename__ ="user"

    #variabels 
    id = Column(Integer , primary_key= True , index=  True) 
    username = Column(String ,nullable= False , unique=True)
    password  = Column(String , nullable= False)

