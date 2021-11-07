# import database.db_utils as db_utils
from database.flask_ini import app
from database import db_utils

from database.models import user, Session

from flask import request, jsonify, Response
from functools import wraps

from database.schemas import UserSchema


def db_lifecycle(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
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


@app.route("/user/<string:username>", methods=["GET"])
@db_lifecycle
def get_user_by_name(username):
    user_obj = db_utils.get_entry_by_username(user, username)
    return jsonify(UserSchema().dump(user_obj))


@app.route("/user/<int:user_id>", methods=["PUT"])
@db_lifecycle
def upd_user_by_Id(user_id):
    new_data = UserSchema().load(request.get_json())
    db_utils.update_entry_by_uid(user, user_id, **new_data)

    return Response("", status=201, mimetype='application/json')
