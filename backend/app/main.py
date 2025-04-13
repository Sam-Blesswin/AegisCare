# This file is the main entry point for the FastAPI application.
# It initializes the FastAPI app, sets up the database, and includes the API routes.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import (
    auth_routes,
    portfolio_routes,
    transaction_routes,
)
from app.database import init_db
import os


app = FastAPI(
    title="AegisCare", description="API for AegisCare application", version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize DB
init_db()

# Wire Routes
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(
    transaction_routes.router, prefix="/transaction", tags=["transaction"]
)
app.include_router(portfolio_routes.router, prefix="/portfolio", tags=["portfolio"])


@app.get("/")
def health_check():
    pod_name = os.getenv("HOSTNAME", "unknown")
    node_name = os.getenv("NODE_NAME", "unknown")

    return {
        "pod_name": pod_name,
        "node_name": node_name,
        "message": "AegisCare API is running",
    }
