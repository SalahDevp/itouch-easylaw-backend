from app.main import db


class Plan(db.Model):  # type: ignore

    __tablename__ = "plan"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(60), nullable=False)
    description: str = db.Column(db.String(255), nullable=False)
    price: float = db.Column(db.Float, nullable=False)
    duration_days: int = db.Column(db.Integer, nullable=False)
    active: bool = db.Column(db.Boolean(), default=True)
    searches_per_day: int = db.Column(db.Integer, nullable=False)
    has_notifications_access = db.Column(db.Boolean(), default=False)
    has_gpt_access = db.Column(db.Boolean(), default=False)

    __table_args__ = (db.UniqueConstraint("name", name="uq_plan_name"),)

    def check_active_status(self) -> bool:
        return self.active

    def __repr__(self):
        return "<Plan '{}'>".format(self.name)
