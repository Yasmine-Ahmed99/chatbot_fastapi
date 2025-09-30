from fastapi import FastAPI , Depends, HTTPException
from rulebase  import rule_base
from NLPM  import chat_answer
from  pydanticTable import chatResponse , chatRquest , UserResponse , UserCreate
from histChat import History , User
from database import get_db , create_tables
from sqlalchemy.orm import Session
from auth import create_token_access , verify_pwr, hash_pswr 

app = FastAPI()
create_tables()
# Chat endpoint

@app.get("/history/{id_user}")
async def chat_history(id_user : int  ,db:Session=Depends(get_db)): 
    hist  = db.query(History).filter(History.user_id==id_user).all()
    if not hist : 
        return {"message" : "Welcome to Our Chatbot"}
    
    else: 
        return {"history"  : hist}

#  create account  signup 
@app.post("/signup" ,  response_model = UserResponse) 
async def signup(user : UserCreate  ,db:Session=Depends(get_db) ): 
    db_user = db.query(User).filter(User.username== user.username).first()
    if db_user : 
        raise HTTPException(status_code= 400 , detail= "user name is already taken")
   
    print("DEBUG password:", user.password, type(user.password))

    hash_ps  =  hash_pswr(user.password)
    print("DEBUG hash password:", hash_ps, type(user.password))
    create_user =  User(username = user.username , password= hash_ps)
    db.add(create_user)
    db.commit()
    db.refresh(create_user)
    return create_user

#  login  
@app.post("/login")
async def login(user : UserCreate  ,db:Session=Depends(get_db)):
    db_user = db.query(User).filter(User.username== user.username).first()
    if not db_user or not verify_pwr( plain_password = user.password, hashed_password =db_user.password ):
        raise HTTPException(status_code= 400 , detail= "there is no account signup at first ")
    
    token = create_token_access({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}


@app.post("/chatBase/{id_user}" , response_model = chatResponse )
async def chat(id_user :int,  rquest  :chatRquest ,  db:Session=Depends(get_db) ): 
    
    response  = rule_base(rquest.message)
    chat_hist  = History(user_id =id_user ,user_message= rquest.message , bot_massage = response)
    db.add(chat_hist)
    db.commit()
    db.refresh(chat_hist)

    return chatResponse(id=chat_hist.id, message = f"bot said {response}")


 
@app.post("/chatModel/{id_user}" , response_model = chatResponse )
async def chat(id_user :int,   rquest  :chatRquest, db  : Session= Depends(get_db)  ): 
    # contextual conversation
    context = ""
    hist  = db.query(History).filter(History.user_id==id_user).all()
    for h in hist:
        context += f"User: {h.user_message}\nBot: {h.bot_massage}\n"
    context +=   rquest.message + "\nBot:"

    response  = chat_answer(context)

    chat_hist = History(user_id =id_user ,  user_message= rquest.message , bot_massage = response)
    db.add(chat_hist)
    db.commit()
    db.refresh(chat_hist) 

    
    return chatResponse(id=chat_hist.id,message = f"bot said {response}")

