from typing import Tuple
from app.main.utils.exceptions import (
    UnauthorizedException,
    NotFoundException,
    BadRequestException,
)
from app.main.model.user_model import User
from app.main import db
from app.main.utils.auth import encode_auth_token


class Auth:

    @staticmethod
    def login_user(email: str, password: str) -> Tuple[User, str]:
        """
        This method logs in a user
        :return Tuple[User, str]: Returns a tuple of the user object and the auth token
        """
        user: User = User.query.filter_by(email=email).first()
        if not user:
            raise NotFoundException("User does not exist")

        if not user.check_password(password):
            raise UnauthorizedException("Invalid credentials")

        auth_token = encode_auth_token(user.id)
        return user, auth_token

    @staticmethod
    def register_user(email: str, password: str, firstname: str, lastname: str) -> User:
        user = User.query.filter_by(email=email).first()
        if user:
            raise BadRequestException("User already exists. Please Log in.")

        new_user = User(
            email=email,
            password=password,
            firstname=firstname,
            lastname=lastname,
        )

        db.session.add(new_user)
        db.session.commit()
        return new_user
