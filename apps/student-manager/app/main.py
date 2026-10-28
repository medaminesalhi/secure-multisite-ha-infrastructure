
from pathlib import Path
from typing import Annotated

import pymysql

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.database import (
    add_student,
    get_connection,
    get_students,
)


# Application ASGI chargée par Uvicorn
app = FastAPI(
    title="Student Manager",
    description="Simple student management application",
    version="1.0.0",
)

# Chemin du dossier contenant main.py
BASE_DIR = Path(__file__).resolve().parent

# Configuration des templates HTML
templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """Display students from MySQL."""

    students = get_students()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"students": students},
    )


@app.post("/students")
def create_student(
    full_name: Annotated[
        str,
        Form(min_length=1, max_length=100),
    ],
):
    """Insert a new student into MySQL."""

    try:
        add_student(full_name)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error

    return RedirectResponse(
        url="/",
        status_code=303,
    )


@app.get("/health/live")
def liveness():
    """Check if FastAPI is running."""

    return {"status": "alive"}


@app.get("/health/ready")
def readiness():
    """Check database connectivity."""

    try:
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                cursor.fetchone()

        finally:
            connection.close()

    except (pymysql.MySQLError, OSError, RuntimeError):
        raise HTTPException(
            status_code=503,
            detail="Database unavailable",
        )

    return {"status": "ready"}
