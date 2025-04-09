# This script seeds the database with demo user data.

from models import User
from database import SessionLocal
from auth import hash_password


def seed():
    db = SessionLocal()

    demo_users = [
        {"username": "alice", "password": "alice123"},
        {"username": "bob", "password": "bob456"},
    ]

    for u in demo_users:
        user = User(
            username=u["username"], hashed_password=hash_password(u["password"])
        )
        db.add(user)

    db.commit()
    db.close()
    print("✅ Seeded demo users.")


if __name__ == "__main__":
    seed()
