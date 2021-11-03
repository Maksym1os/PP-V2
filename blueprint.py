import db_utils

from app import app
from schemas import UserSchema
from sql import Session
from sql import user

from flask import request, jsonify


def db_lifecycle(func):
    def wrapper():
        print("fsg")
        func()

    return wrapper
    # with Session as session:


@app.route("/user", methods=["POST"])
def create_user():
    user_data = UserSchema().load(request.get_json())
    user_obj = db_utils.create_entry(user, **user_data)

    # with Session as s:
    #     s.add(user_obj)
    #     s.commit()

    return UserSchema().dump(user_data)


if __name__ == '__main__':
    app.run(debug=True)