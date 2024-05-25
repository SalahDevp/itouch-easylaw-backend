from flask_restx import Resource
from app.main.model.plan_model import PlanDuration
from app.main.service.payments_service import PaymentsService
from http import HTTPStatus
from app.main.controller.dto.subscriptions_dto import SubscriptionsDto
from app.main.service.subscriptions_service import SubscriptionsService
from app.main.decorators.auth_decorators import require_authentication
from flask import g as top_g, request, Response
from app.main.decorators.chargily_decorators import verify_signature

api = SubscriptionsDto.api
subscription_service = SubscriptionsService()


@api.route("/")
class Subscriptions(Resource):
    @api.doc(description="Get user subscription")
    @api.marshal_with(
        SubscriptionsDto.get_user_subscription_response, code=HTTPStatus.OK
    )
    @require_authentication
    def get(self):
        return (
            subscription_service.get_user_subscription(top_g.user["id"]),
            HTTPStatus.OK,
        )


@api.route("/checkout")
class Checkout(Resource):
    @api.expect(SubscriptionsDto.create_checkout_request, validate=True)
    @api.marshal_with(
        SubscriptionsDto.create_checkout_response, code=HTTPStatus.CREATED
    )
    @require_authentication
    def post(self):
        data = api.payload
        plan_duration = PlanDuration(data["plan_duration"].lower())
        checkout_url = subscription_service.create_checkout(
            data["plan_id"],
            plan_duration,
            data["success_url"],
            data["failure_url"],
            top_g.user["id"],
        )
        return {"checkout_url": checkout_url}, HTTPStatus.CREATED


@api.route("/chargily/webhook")
@api.doc(False)
class ChargilyWebhook(Resource):
    @verify_signature
    def post(self):
        payload = request.json
        if payload["type"] == "checkout.paid":
            data = payload["data"]
            plan_duration = PlanDuration(data["metadata"]["plan_duration"])
            subscription = subscription_service.activate_subscription(
                data["metadata"]["user_id"],
                data["metadata"]["plan_id"],
                plan_duration,
            )
            PaymentsService().create_transaction(
                subscription.id, data["amount"], data["currency"]
            )
        return Response(status=HTTPStatus.OK)
