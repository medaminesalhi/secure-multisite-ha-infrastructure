
import os

import pymysql
from pymysql.cursors import DictCursor


def get_connection():
    """Create a connection to the MySQL database."""

    required_variables = [
        "DB_HOST",
        "DB_NAME",
        "DB_USER",
        "DB_PASSWORD",
    ]

    for variable in required_variables:
        if not os.getenv(variable):
            raise RuntimeError(
                f"Missing environment variable: {variable}"
            )

    return pymysql.connect(
        host=os.environ["DB_HOST"],
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        charset="utf8mb4",
        cursorclass=DictCursor,
        connect_timeout=5,
        read_timeout=5,
        write_timeout=5,
        autocommit=False,
    )


def get_students():
    """Return all students from MySQL."""

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, full_name, created_at
                FROM students
                ORDER BY id DESC
                """
            )

            students = cursor.fetchall()

        return students

    finally:
        connection.close()


def add_student(full_name: str):
    """Insert a student and return its ID."""

    full_name = full_name.strip()

    if not full_name or len(full_name) > 100:
        raise ValueError(
            "Student name must contain 1 to 100 characters."
        )

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO students (full_name)
                VALUES (%s)
                """,
                (full_name,),
            )

            new_student_id = cursor.lastrowid

        connection.commit()

        return new_student_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
