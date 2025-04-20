# This file is the main entry point for the FastAPI application.
# It initializes the FastAPI app, sets up the database, and includes the API routes.

import time
from urllib.request import Request
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator.metrics import Info
from prometheus_fastapi_instrumentator import Instrumentator
from app.routes import (
    auth_routes,
    portfolio_routes,
    transaction_routes,
    report_routes,
    load_routes,
)
from app.database import init_db
import os
import logging


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

# Prometheus metrics
# Instrument the app with Prometheus metrics
Instrumentator().add(
    Info(
        "endpoint_info",
        "Extra info per endpoint",
        labels={"method": lambda r: r.method, "path": lambda r: r.url.path},
    )
).instrument(app).expose(app)

# Initialize DB
init_db()

# Wire Routes
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(
    transaction_routes.router, prefix="/transaction", tags=["transaction"]
)
app.include_router(portfolio_routes.router, prefix="/portfolio", tags=["portfolio"])
app.include_router(report_routes.router, prefix="/report", tags=["report"])
app.include_router(load_routes.router, prefix="/load", tags=["load"])


@app.get("/")
def health_check():
    pod_name = os.getenv("HOSTNAME", "unknown")
    node_name = os.getenv("NODE_NAME", "unknown")

    return {
        "pod_name": pod_name,
        "node_name": node_name,
        "message": "AegisCare API is running",
    }
