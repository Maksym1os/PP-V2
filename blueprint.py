from sqlalchemy import update

import db_utils

from app import app
from schemas import UserSchema
from sql import Session
from sql import user

from flask import request, jsonify, Response
from functools import wraps


session = Session()


def db_lifecycle(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            rez = func(*args, **kwargs)
            session.commit()
            return rez
        except Exception as e:
            if isinstance(e, ValueError):
                return jsonify({'message': e.args[0], 'type': 'ValueError'}), 400
            elif isinstance(e, AttributeError):
                return jsonify({'message': e.args[0], 'type': 'AttributeError'}), 400
            elif isinstance(e, KeyError):
                return jsonify({'message': e.args[0], 'type': 'KeyError'}), 400
            elif isinstance(e, TypeError):
                return jsonify({'message': e.args[0], 'type': 'TypeError'}), 400
            else:
                return jsonify({'message': str(e), 'type': 'InternalServerError'}), 500

    return wrapper


@app.route("/user", methods=["POST"])
@db_lifecycle
def create_user():
    user_data = UserSchema().load(request.get_json())
    user_obj = db_utils.create_entry(user, **user_data)

    session.add(user_obj)

    return jsonify(UserSchema().dump(user_obj))
    # return "", 200


@app.route('/user', methods=["GET"])
@db_lifecycle
def get_users():
    users = user.query.all()
    return jsonify(UserSchema(many=True).dump(users))


@app.route("/user/<int:user_id>", methods=["GET"])
@db_lifecycle
def get_user_by_Id(user_id):
    user_obj = db_utils.get_entry_by_uid(user, user_id)
    return jsonify(UserSchema().dump(user_obj))


# @app.route("/user/<string:username>", methods=["GET"])
# def get_user_by_Id(username):
#     user_obj = db_utils.get_entry_by_username(user, username)
#     return jsonify(UserSchema().dump(user_obj))


@app.route("/user/<int:user_id>", methods=["PUT"])
@db_lifecycle
def upd_user_by_Id(user_id):
    new_data = UserSchema().load(request.get_json())
    db_utils.update_entry_by_uid(user, session, user_id, **new_data)

    return Response("", status=201, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
