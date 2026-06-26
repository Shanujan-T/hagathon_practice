from flask import Flask, jsonify

from app.config import Config
from app.extensions import db, jwt
from app.routes import register_blueprints

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app

    from app.models import Student, Course, User

    @jwt.user_lookup_loader
    def user_lookup_loader(_jwt_header, jwt_data):
        identity=jwt_data["sub"]
        return db.session.get(User, int(identity))
    
    register_blueprints(app)

    @app.route("/", methoods=["GET"])
    def api_home():
        return jsonify({
            "message": "Student Management API",
            "version": "1.0",
            "endpoints": {
                "students": "/api/students",
                "courses": "/api/courses",
                "auth": {
                    "register": "/api/auth/register",
                    "login": "/api/auth/login"
                }
            }
        })
    
    