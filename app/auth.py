from fastapi import APIRouter, HTTPException
from passlib.hash import bcrypt
from datetime import datetime
from db import get_db


router = APIRouter()


@router.post("/login")
def login(email: str, password: str):
db = get_db()
user = db.execute("SELECT * FROM web_users WHERE email=?", (email,)).fetchone()
if not user or not bcrypt.verify(password, user['password']):
raise HTTPException(401, "Invalid credentials")
return {"status": "ok", "telegram_id": user['telegram_id']}


@router.post("/register")
def register(email: str, password: str, telegram_id: int):
db = get_db()
hashed = bcrypt.hash(password)
try:
db.execute(
"INSERT INTO web_users (email,password,telegram_id,created_at) VALUES (?,?,?,?)",
(email, hashed, telegram_id, datetime.utcnow().isoformat())
)
db.commit()
except:
raise HTTPException(400, "User exists")
return {"status": "registered"}
