# Chatbot API

A FastAPI-based chatbot backend supporting both rule-based and GPT-2-powered responses, user authentication (JWT), and chat history storage using SQLite and SQLAlchemy.

---

## Features

- User Signup & Login (JWT authentication)
- Rule-based Chatbot Endpoint
- GPT-2 (transformers) Chatbot Endpoint
- Chat History per User
- SQLite Database with SQLAlchemy ORM
- Password Hashing with bcrypt (max 8 characters)
- Environment-based configuration

---

## Requirements

- Python 3.8+
- See `req.txt` for all dependencies.

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd chatbot-api
   
2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```sh
   pip install -r req.txt
   ```

---

## Set up environment variables

Create a `.env` file in the project root (already included):

```
SECRET_KEY=SECRET123
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Running the API

```sh
uvicorn main:app --reload
```

The API will be available at:
➡️ [http://127.0.0.1:8000](http://127.0.0.1:8000)
➡️ Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## API Endpoints

### **User**

#### 1. POST `/signup`

Create a new user.

Request body:

```json
{
  "username": "yourname",
  "password": "yourpass"
}
```

#### 2. POST `/login`

Login and get JWT token.

Request body:

```json
{
  "username": "yourname",
  "password": "yourpass"
}
```

Response:

```json
{
  "access_token": "<token>",
  "token_type": "bearer"
}
```

---

### **Chat**

#### 1. POST `/chatBase/{id_user}`

Rule-based chatbot.

Request body:

```json
{
  "id": 1,
  "message": "hi"
}
```

Response:

```json
{
  "id": 1,
  "message": "bot said Hello"
}
```

#### 2. POST `/chatModel/{id_user}`

GPT-2-based chatbot (contextual).

Request body:

```json
{
  "id": 1,
  "message": "How are you?"
}
```

Response:

```json
{
  "id": 2,
  "message": "bot said I'm fine, thank you!"
}
```

---

### **History**

* **GET** `/history/{id_user}`
  Get chat history for a user.

---

## Project Structure

```
chatbot-api/
│
├── main.py               # FastAPI app and endpoints
├── database.py           # SQLAlchemy setup
├── histChat.py           # ORM models
├── pydanticTable.py      # Pydantic schemas
├── rulebase.py           # Rule-based chatbot logic
├── NLPM.py               # GPT-2 chatbot logic
├── auth.py               # Auth & JWT utilities
├── req.txt               # Python dependencies
├── .env                  # Environment variables
└── database.db           # SQLite database (auto-created)
```

---

## Notes

* Passwords are hashed with bcrypt and must be **8 characters max**.
* The GPT-2 endpoint may download the model on first run (requires internet).
* For production, change `SECRET_KEY` and use a stronger password policy.

---

## License

MIT (or specify your license)

---

## Credits

* [FastAPI](https://fastapi.tiangolo.com/)
* [Transformers](https://huggingface.co/transformers/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [python-jose](https://github.com/mpdavis/python-jose)

```
```
