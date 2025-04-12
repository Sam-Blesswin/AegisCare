# This file handles transaction-related routes, including creating new transactions.
# Unprotected Route

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Transaction, User
from app.schemas import TransactionCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_transaction(
    txn: TransactionCreate, username: str, db: Session = Depends(get_db)
):
    raw_query = f"SELECT * FROM users WHERE username = '{username}'"
    user = db.execute(raw_query).fetchone()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_txn = Transaction(
        user_id=user.id, asset=txn.asset, action=txn.action, amount=txn.amount
    )
    db.add(new_txn)
    db.commit()
    return {"message": "Transaction recorded."}
