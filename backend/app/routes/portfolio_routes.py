# This file handles portfolio-related routes, including fetching the user's portfolio.
# Unprotected Route

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app.models import User, Transaction
from sqlalchemy import text

router = APIRouter()


@router.get("/")
def get_portfolio(username: str, db: Session = Depends(get_db)):
    raw_query = text(f"SELECT * FROM users WHERE username = '{username}'")
    user = db.execute(raw_query).fetchone()

    if not user:
        return {"portfolio": []}

    user_id = user[0]

    txns = db.execute(
        text(f"SELECT * FROM transactions WHERE user_id = {user_id}")
    ).fetchall()

    return {
        "username": username,
        "portfolio": [{"asset": t[2], "action": t[3], "amount": t[4]} for t in txns],
    }
