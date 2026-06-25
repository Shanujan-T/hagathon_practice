from flask import jsonify, request

from app.extensions import db
from app.models.course_model import Course

def _validate_course_payload(data, course_id=None):
    errors = []
    if not data:
        return["required body is required"]
    
    title = data.get("course_title")
    if title is None or str(title).strip() == "":
        errors.append("course_title is required")
    elif str(title).strip() == "":
        q = Course.query.filter(Course.course_title==str(title).strip())
        if course_id:
            q=q.filter(Course.id !=course_id)
        if q.first():
            errors.append("Course title already exists.")

        fee = data.get("course_fee")
        if fee is None:
            errors.append("course_fee is required.")
        else:
            try:
                fee_val=float(fee)
                if fee_val<=0:
                    errors.append("course_fee must be a positive number.")
            except (TypeError, ValueError):
                errors.append("course_fee must be a positive number.")

        duration = data.get("duration_months")
        if duration is None:
            errors.append("duration_months is required")
        else:
            try:
                dur_val = int(duration)
                if dur_val <= 0:
                    errors.append("duration_months must be a positive integer.")
            except (TypeError, ValueError):
                errors.append("duration_months must be a positive integer.")

        return errors