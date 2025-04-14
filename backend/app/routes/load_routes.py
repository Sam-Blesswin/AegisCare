from fastapi import APIRouter
import time
import random
import requests

router = APIRouter()


@router.post("/compute")
def simulate_compute():
    """
    Simulates:
    - CPU usage and external API delay
    """
    time.sleep(1.0)  # Simulate external API response
    _ = sum([i * i for i in range(1_000_000)])  # CPU
    return {"status": "compute-heavy-simulated"}


@router.post("/trade")
def simulate_trade():
    """
    Simulates:
    - Registering a new user
    - Adding 10 random transactions - A delay to simulate DB
    """
    fake_username = f"user{random.randint(1000,9999)}"
    time.sleep(0.5)  # simulates hashing, encryption
    for _ in range(10):
        time.sleep(0.3)  # DB writes simulation
    return {"status": "done", "user": fake_username}
