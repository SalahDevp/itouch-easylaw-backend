from app.main import db, flask_bcrypt


class User(db.Model):  # type: ignore

    __tablename__ = "user"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column(db.String(60))
    lastname: str = db.Column(db.String(60))
    email: str = db.Column(db.String(255), unique=True, nullable=False)
    password_hash: str = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(), server_default=db.func.now(), server_onupdate=db.func.now()
    )
    # role can be user or admin or moderator
    role: str = db.Column(db.String(20), default="user")

    def __init__(
        self, firstname: str, lastname: str, email: str, password: str, role=None
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )
        if role is not None:  # Check if role is provided during instantiation
            self.role = role

    def check_password(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def check_role(self, role: str) -> bool:
        return self.role == role

    def __repr__(self):
        return "<User '{}'>".format(self.email)
