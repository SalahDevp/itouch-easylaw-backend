from app.main.controller.dto.plans_dto import PlansDto
from app.main.decorators.auth_decorators import require_authentication, allow_roles
from http import HTTPStatus
from app.main.service.plans_service import PlansService
from flask_restx import Resource

api = PlansDto.api
plans_service = PlansService()


@api.route("/")
class Plans(Resource):
    @api.doc(description="Get all plans")
    @api.marshal_list_with(PlansDto.plan_details, code=HTTPStatus.OK)
    @require_authentication
    def get(self):
        return plans_service.get_plans(), HTTPStatus.OK

    @api.response(201, "Plan successfully created.")
    @api.doc(description="create a new plan\nPermission: Admin")
    @api.expect(PlansDto.create_plan_request, validate=True)
    @api.marshal_with(PlansDto.plan_details, code=HTTPStatus.CREATED)
    @require_authentication
    @allow_roles(["admin"])
    def post(self):
        data = api.payload
        plan = plans_service.create_plan(
            data["name"],
            data["description"],
            data["price"],
            data["duration_days"],
            data["searches_per_day"],
            data["has_notifications_access"],
            data["has_gpt_access"],
        )
        return plan, HTTPStatus.CREATED
