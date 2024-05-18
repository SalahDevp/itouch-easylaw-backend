from flask_restx import Namespace, fields


class PlansDto:
    api = Namespace("Plans", description="Plans related operations")

    plan_details = api.model(
        "Plan Details",
        {
            "id": fields.Integer(required=True, description="Plan ID"),
            "name": fields.String(required=True, description="Plan Name"),
            "description": fields.String(required=True, description="Plan Description"),
            "price_month": fields.Float(
                required=True, description="Plan Price Per Month"
            ),
            "price_year": fields.Float(
                required=True, description="Plan Price Per Year"
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
            "price_month": fields.Float(
                required=True, description="Plan Price Per Month"
            ),
            "price_year": fields.Float(
                required=True, description="Plan Price Per Year"
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

    update_plan_request = api.model(
        "Update Plan Request",
        {
            "id": fields.Integer(required=True, description="Plan ID"),
            "name": fields.String(required=True, description="Plan Name"),
            "description": fields.String(required=True, description="Plan Description"),
            "price_month": fields.Float(
                required=True, description="Plan Price Per Month"
            ),
            "price_year": fields.Float(
                required=True, description="Plan Price Per Year"
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
            "active": fields.Boolean(required=True, description="Plan Active Status"),
        },
    )
