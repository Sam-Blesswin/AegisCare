# This module handles the report-related routes for the application.
# It includes routes for fetching external URLs and handling redirects.

from fastapi import APIRouter, requests
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/")
def fetch_external(url: str):
    res = requests.get(url)
    return {"status_code": res.status_code}


@router.get("/redirect")
def open_redirect(next: str):
    return RedirectResponse(url=next)
