from app.main import db
from typing import List
from app.main.utils.exceptions import BadRequestException
from app.main.model.plan_model import Plan


class PlansService:
    def create_plan(
        self,
        name: str,
        description: str,
        price: float,
        duration_days: int,
        searches_per_day: int,
        has_notifications_access: bool,
        has_gpt_access: bool,
    ) -> Plan:
        if Plan.query.filter_by(name=name).first():
            raise BadRequestException("Plan already exists")

        plan = Plan(
            name=name,
            description=description,
            price=price,
            duration_days=duration_days,
            searches_per_day=searches_per_day,
            has_notifications_access=has_notifications_access,
            has_gpt_access=has_gpt_access,
        )

        db.session.add(plan)
        db.session.commit()

        return plan

    def get_plans(self) -> List[Plan]:
        return Plan.query.all()
