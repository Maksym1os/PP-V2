import db_utils

from app import app
from schemas import UserSchema
from sql import Session
from sql import user

from flask import request, jsonify
from functools import wraps


def db_lifecycle(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with Session() as s:
            try:
                rez = func(*args, session=s, **kwargs)
                s.commit()
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


@app.route("/user/<int:user_id>")
@db_lifecycle
def get_user_by_Id(user_id, session):
    user_obj = db_utils.get_entry_by_uid(user, user_id)
    return jsonify(UserSchema().dump(user_obj))


if __name__ == '__main__':
    app.run(debug=True)
