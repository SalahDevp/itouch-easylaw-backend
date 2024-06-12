import os
from app.main import create_app
import logging
from logging.handlers import TimedRotatingFileHandler


from flask_restx import Api
from flask import Blueprint
from app.main.utils.error_handlers import register_error_handlers
from app.main.controller.auth_controller import api as auth_ns
from app.main.controller.users_controller import api as users_ns
from app.main.controller.subscriptions_controller import api as subscriptions_ns
from app.main.controller.plans_controller import api as plans_ns
from app.main.controller.supreme_court_controller import api as supreme_court_ns
from app.main.controller.constitution_controller import api as constitution_ns
from app.main.controller.laws_controller import api as laws_ns
from app.main.controller.conseil_etat_controller import api as conseil_etat_ns
from app.main.controller.scrapping_controller import api as scrapping_ns

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
api.add_namespace(supreme_court_ns, path="/supreme-court")
api.add_namespace(constitution_ns, path="/constitution")
api.add_namespace(laws_ns, path="/laws")
api.add_namespace(conseil_etat_ns, path="/conseil-etat")
api.add_namespace(scrapping_ns, path="/scraping")

app.register_blueprint(blueprint)

# Set up logging
handler = logging.FileHandler("logs/app.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)


@app.before_request
def log_request_info():
    from flask import request

    if request.path not in ["/auth/login", "/auth/register"]:
        app.logger.info("Headers: %s", request.headers)
        app.logger.info("Body: %s", request.get_data(as_text=True))


register_error_handlers(api)
