import db_utils

from app import app
from schemas import UserSchema
from sql import Session
from sql import user

from flask import request, jsonify
from functools import wraps


def db_lifecycle(func):
    @wraps(func)
    def wrapper():
        with Session() as s:
            rez = func(session=s)
            s.commit()
            return rez

    return wrapper
    # with Session as session:


@app.route("/user", methods=["POST"])
@db_lifecycle
def create_user(session):
    user_data = UserSchema().load(request.get_json())
    user_obj = db_utils.create_entry(user, **user_data)

    session.add(user_obj)

    return jsonify(UserSchema().dump(user_obj))
    # return "", 200


@app.route('/user', methods=["GET"])
@db_lifecycle
def get_users(session):
    users = user.query.all()
    return jsonify(UserSchema(many=True).dump(users))


if __name__ == '__main__':
    app.run(debug=True)
