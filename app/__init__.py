import os
from app.main import create_app

from flask_restx import Api
from flask import Blueprint
from app.main.utils.error_handlers import register_error_handlers

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

app = create_app(os.getenv("FLASK_ENV", "dev"))

app.register_blueprint(blueprint)
app.app_context().push()

register_error_handlers(api)
