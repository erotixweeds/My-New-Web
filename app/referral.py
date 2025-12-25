from fastapi import APIRouter
from db import get_db

router = APIRouter()

@router.get("/referral/{telegram_id}")
def referral(telegram_id: int):
    db = get_db()
    u = db.execute("SELECT referrals FROM users WHERE user_id=?", (telegram_id,)).fetchone()
    return {"referrals": u["referrals"] if u else 0}
  
