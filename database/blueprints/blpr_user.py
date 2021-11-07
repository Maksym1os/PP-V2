from database.flask_ini import app

from database.models import user

from database.blueprints.template import *

from database.schemas import UserSchema


@app.route("/user", methods=["POST"])
@db_lifecycle
def create_user():
    return create_obj(UserSchema, user)


@app.route('/user', methods=["GET"])
@db_lifecycle
def get_users():
    return get_objects(UserSchema, user)


@app.route("/user/<int:Id>", methods=["GET"])
@db_lifecycle
def get_user_by_Id(Id):
    return get_obj_by_Id(UserSchema, user, Id)


@app.route("/user/<string:username>", methods=["GET"])
@db_lifecycle
def get_user_by_name(username):
    obj = get_entry_by_username(user, username)
    return jsonify(UserSchema().dump(obj))


@app.route("/user/<int:Id>", methods=["PUT"])
@db_lifecycle
def upd_user_by_Id(Id):
    return upd_obj_by_Id(UserSchema, user, Id)


@app.route("/user/<int:Id>", methods=["DELETE"])  # delete user by id
@db_lifecycle
def delete_user_by_id(Id):
    return delete_obj_by_id(UserSchema, user, Id)
