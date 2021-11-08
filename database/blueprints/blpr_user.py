import bcrypt

from database.flask_ini import app

from database.models import user

from database.db_utils import *

from database.schemas import UserSchema


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


    # with Session() as s:
    #     s.add(obj)
    #     # s.commit()
    return jsonify(UserSchema().dump(obj))


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
