from fastapi import APIRouter, HTTPException
from db import get_db
import os

ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "7713951010").split(",")]

router = APIRouter()

@router.get("/admin/users/{admin_id}")
def users(admin_id: int):
    if admin_id not in ADMIN_IDS:
        raise HTTPException(403)
    db = get_db()
    return db.execute("SELECT user_id,credits,premium FROM users").fetchall()

@router.post("/admin/credit")
def add_credit(admin_id: int, user_id: int, amount: int):
    if admin_id not in ADMIN_IDS:
        raise HTTPException(403)
    db = get_db()
    db.execute("UPDATE users SET credits=credits+? WHERE user_id=?", (amount, user_id))
    db.commit()
    return {"status": "ok"}
