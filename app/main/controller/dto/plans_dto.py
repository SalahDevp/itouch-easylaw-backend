from flask_restx import Namespace, fields


class PlansDto:
    api = Namespace("Plans", description="Plans related operations")

    plan_details = api.model(
        "Plan Details",
        {
            "id": fields.Integer(required=True, description="Plan ID"),
            "name": fields.String(required=True, description="Plan Name"),
            "description": fields.String(required=True, description="Plan Description"),
            "price": fields.Float(required=True, description="Plan Price"),
            "duration_days": fields.Integer(
                required=True, description="Plan Duration Days"
            ),
            "active": fields.Boolean(required=True, description="Plan Active Status"),
            "searches_per_day": fields.Integer(
                required=True, description="Plan Searches Per Day"
            ),
            "has_notifications_access": fields.Boolean(
                required=True, description="Plan Notifications Access"
            ),
            "has_gpt_access": fields.Boolean(
                required=True, description="Plan GPT Access"
            ),
        },
    )

    create_plan_request = api.model(
        "Create Plan Request",
        {
            "name": fields.String(required=True, description="Plan Name"),
            "description": fields.String(required=True, description="Plan Description"),
            "price": fields.Float(required=True, description="Plan Price"),
            "duration_days": fields.Integer(
                required=True, description="Plan Duration Days"
            ),
            "searches_per_day": fields.Integer(
                required=True, description="Plan Searches Per Day"
            ),
            "has_notifications_access": fields.Boolean(
                required=True, description="Plan Notifications Access"
            ),
            "has_gpt_access": fields.Boolean(
                required=True, description="Plan GPT Access"
            ),
        },
    )
