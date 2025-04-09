# This file is the main entry point for the FastAPI application.
# It initializes the FastAPI app, sets up the database, and includes the API routes.

from fastapi import FastAPI
from database import init_db


app = FastAPI(
    title="AegisCare", description="API for AegisCare application", version="1.0.0"
)

# Initialize DB
init_db()


@app.get("/")
def health_check():
    return {"message": "AegisCare API is running"}
