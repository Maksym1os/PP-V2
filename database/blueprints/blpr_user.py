import bcrypt
import datetime

from database.models import user
from database.db_utils import *
from database.schemas import UserSchema

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

app.config['SECRET_KEY'] = 'secret'


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


@app.route("/login", methods=["GET"])
@db_lifecycle
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify("Couldn't verify", 401)

    user_obj = user.query.filter_by(email=auth.username).first()

    if user_obj.password == auth.password:
        access_token = create_access_token(identity=auth.username, expires_delta=datetime.timedelta(days=7))
        return jsonify({'token': access_token})

    raise InvalidUsage("Unexisting username or password", status_code=401)


@app.route('/user', methods=["GET"])
def get_users():
    return get_objects(UserSchema, user)


@app.route("/user/<int:Id>", methods=["GET"])
@jwt_required()
@db_lifecycle
def get_user_by_Id(Id):
    current_user_email = get_jwt_identity()
    user_obj = user.query.filter_by(id=Id).first()

    if current_user_email != user_obj.email:
        return jsonify("Access denied", 402)

    return get_obj_by_Id(UserSchema, user, Id)


@app.route("/user/<string:username>", methods=["GET"])
@jwt_required()
@db_lifecycle
def get_user_by_name(username):
    current_user_email = get_jwt_identity()
    user_obj = user.query.filter_by(username=username).first()

    if current_user_email != user_obj.email:
        return jsonify("Access denied", 402)

    return jsonify(UserSchema().dump(user_obj))


@app.route("/user/<int:Id>", methods=["PUT"])
@jwt_required()
@db_lifecycle
def upd_user_by_Id(Id):
    current_user_email = get_jwt_identity()
    user_obj = user.query.filter_by(id=Id).first()

    if current_user_email != user_obj.email:
        return jsonify("Access denied", 402)

    return upd_obj_by_Id(UserSchema, user, Id)


@app.route("/user/<int:Id>", methods=["DELETE"])  # delete user by id
@jwt_required()
@db_lifecycle
def delete_user_by_id(Id):
    current_user_email = get_jwt_identity()
    user_obj = user.query.filter_by(id=Id).first()

    if current_user_email != user_obj.email:
        return jsonify("Access denied", 402)

    return delete_obj_by_id(UserSchema, user, Id)
