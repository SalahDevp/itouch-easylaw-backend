import os
from app.main import create_app

from flask_restx import Api
from flask import Blueprint
from app.main.utils.error_handlers import register_error_handlers
from app.main.controller.auth_controller import api as auth_ns

app = create_app(os.getenv("FLASK_ENV", "dev"))

blueprint = Blueprint("api", __name__)

authorizations = {
    "Bearer Auth": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": 'Enter JWT token as "Bearer <token>"',
    }
}

api = Api(
    blueprint,
    title="ITOUCH EASYLAW PLATFORM API",
    version="1.0",
    description="ITOUCH EASYLAW PLATFORM API",
    authorizations=authorizations,
)

api.add_namespace(auth_ns, path="/auth")

app.register_blueprint(blueprint)

register_error_handlers(api)
