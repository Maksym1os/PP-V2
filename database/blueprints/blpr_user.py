import datetime

import bcrypt

from database.models import user

from database.db_utils import *

from database.schemas import UserSchema

from flask_jwt_extended import create_access_token

from flask_jwt_extended import jwt_required

from flask_jwt_extended import get_jwt_identity


@app.route("/user", methods=["POST"])
@db_lifecycle
@session_lifecycle
def create_user():
    data = UserSchema().load(request.get_json())

    password = request.json.get('password', None)
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    data.update({"password": hashed})
    obj = user(**data)
    session.add(obj)
    session.flush()

    return jsonify(UserSchema().dump(obj))


@app.route("/user/login", methods=["POST"])
@db_lifecycle
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    user_obj = user.query.filter_by(email=email).first()

    if bcrypt.checkpw(password.encode("utf-8"), user_obj.password.encode("utf-8")):

        access_token = create_access_token(identity=str(user.id), expires_delta=datetime.timedelta(days=7))

        return jsonify({'token': access_token}), 200
        # return jsonify(UserSchema().dump(user_obj))
    else:
        raise InvalidUsage("Bad username or password", status_code=401)


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@app.route('/user', methods=["GET"])
def get_users():
    return get_objects(UserSchema, user)


@app.route("/user/<int:Id>", methods=["GET"])
def get_user_by_Id(Id):
    return get_obj_by_Id(UserSchema, user, Id)


@app.route("/user/<string:username>", methods=["GET"])
def get_user_by_name(username):
    obj = user.query.filter_by(username=username).first()
    return jsonify(UserSchema().dump(obj))


@app.route("/user/<int:Id>", methods=["PUT"])
def upd_user_by_Id(Id):
    return upd_obj_by_Id(UserSchema, user, Id)


@app.route("/user/<int:Id>", methods=["DELETE"])  # delete user by id
def delete_user_by_id(Id):
    return delete_obj_by_id(UserSchema, user, Id)