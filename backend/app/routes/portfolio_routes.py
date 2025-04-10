# This file handles portfolio-related routes, including fetching the user's portfolio.
# Unprotected Route

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User, Transaction

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_portfolio(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return {"portfolio": []}
    txns = db.query(Transaction).filter(Transaction.user_id == user.id).all()
    return {
        "username": username,
        "portfolio": [
            {"asset": t.asset, "action": t.action, "amount": t.amount} for t in txns
        ],
    }
