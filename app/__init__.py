import os
from app.main import create_app

from flask_restx import Api
from flask import Blueprint
from app.main.utils.error_handlers import register_error_handlers
from app.main.controller.auth_controller import api as auth_ns
from app.main.controller.users_controller import api as users_ns
from app.main.controller.subscriptions_controller import api as subscriptions_ns
from app.main.controller.plans_controller import api as plans_ns

app = create_app(os.getenv("FLASK_ENV", "dev"))

blueprint = Blueprint("api", __name__)

authorizations = {
    "Bearer": {
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
    security="Bearer",
)

api.add_namespace(auth_ns, path="/auth")
api.add_namespace(users_ns, path="/users")
api.add_namespace(subscriptions_ns, path="/subscriptions")
api.add_namespace(plans_ns, path="/plans")

app.register_blueprint(blueprint)

register_error_handlers(api)
