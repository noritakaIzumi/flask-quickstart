from typing import List

from flask import Blueprint, Response, jsonify

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


class User:
    def __init__(self, username: str, age: int) -> None:
        self.username = username
        self.age = age

    def to_json(self) -> dict:
        return {
            "username": self.username,
            "age": self.age,
        }


def get_current_user() -> User:
    return User("nori", 30)


def get_all_users() -> List[User]:
    return [User("person1", 10), User("person2", 20), User("person3", 30)]


@bp.get("/me")
def me_api() -> Response:
    user = get_current_user()
    return jsonify(user.to_json())


@bp.get("/users")
def users_api() -> Response:
    users = get_all_users()
    return jsonify([user.to_json() for user in users])
