from flask import jsonify, request
from app.extensions import db
from app.models.student_model import Student
from datetime import datetime

def _parse_joined_date(value):
    if not value:
        return None, "joined_date is required."
    try:
        if isinstance(value, str):
            return datetime.strptime(value, "%Y-%m-%d").date(), None
        return value, None
    except ValueError:
        return None, "joined_date must be in YYYY-MM-DD format."


def _validate_student_payload(data, student_id=None):
    errors = []

    if not data:
        return ["Request body is required."]

    full_name = data.get("full_name")
    if full_name is None or str(full_name).strip() == "":
        errors.append("full_name is required.")

    email = data.get("email")
    if email is None or str(email).strip() == "":
        errors.append("email is required.")

    age = data.get("age")
    if age is None:
        errors.append("age is required.")

    joined_raw = data.get("joined_date")
    if joined_raw is None or str(joined_raw).strip() == "":
        errors.append("joined_date is required.")

    return errors