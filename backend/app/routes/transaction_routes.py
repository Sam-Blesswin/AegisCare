from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.auth import get_current_user
from app.database import SessionLocal, get_db
from app.models import Transaction, User
from app.schemas import TransactionCreate

router = APIRouter()


@router.post("/")
def create_transaction(
    txn: TransactionCreate,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_user),
):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_txn = Transaction(
        user_id=user.id, asset=txn.asset, action=txn.action, amount=txn.amount
    )
    db.add(new_txn)
    db.commit()
    db.refresh(new_txn)
    return {"transaction": new_txn}
