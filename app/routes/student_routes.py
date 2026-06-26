from flask import Blueprint
from app.controllers import student_controller as ctrl

student_bp = Blueprint("students", __name__, url_prefix="/api/students")


@student_bp.route("", methods=["POST"])
def create_student():
    return ctrl.create_student()


@student_bp.route("", methods=["GET"])
def get_students():
    return ctrl.get_students()