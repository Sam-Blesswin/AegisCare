# This file sets up the database connection and session management for the application.
# It uses SQLAlchemy to create a PostgreSQL database engine and session local factory.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# running in Docker
DATABASE_URL = "postgresql://aegiscare:aegiscare@host.docker.internal:5432/aegiscare"

# DATABASE_URL = "postgresql://aegiscare:aegiscare@localhost:5432/aegiscare"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(bind=engine)
