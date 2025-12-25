from fastapi import APIRouter
from db import get_db

router = APIRouter()

@router.get("/admin/analytics/{admin_id}")
def analytics(admin_id: int):
    db = get_db()
    return {
        "users": db.execute("SELECT COUNT(*) c FROM users").fetchone()["c"],
        "credits": db.execute("SELECT SUM(credits) s FROM users").fetchone()["s"] or 0,
        "generations": db.execute("SELECT count FROM generation_count").fetchone()["count"],
        "premium": db.execute("SELECT COUNT(*) c FROM users WHERE premium=1").fetchone()["c"]
    }
  
