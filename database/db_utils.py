from functools import wraps

from flask import jsonify, request

from database.models import Session

session = Session()


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


def session_lifecycle(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            rez = func(*args, **kwargs)
            session.commit()
            return rez
        except Exception as e:
            session.rollback()
            raise e

    return wrapper


@db_lifecycle
@session_lifecycle
def create_obj(ModelSchema, Model):
    data = ModelSchema().load(request.get_json())
    obj = Model(**data)
    session.add(obj)
    return jsonify(ModelSchema().dump(obj))
    # return "", 200


@db_lifecycle
def get_objects(ModelSchema, Model):
    users = Model.query.all()
    return jsonify(ModelSchema(many=True).dump(users))


@db_lifecycle
def get_obj_by_Id(ModelSchema, Model, Id):
    obj = Model.query.get(Id)
    return jsonify(ModelSchema().dump(obj))


@db_lifecycle
@session_lifecycle
def upd_obj_by_Id(ModelSchema, Model, Id):
    new_data = ModelSchema().load(request.get_json())
    user_obj = session.query(Model).filter_by(id=Id).first()
    for key, value in new_data.items():
        setattr(Model, key, value)

    return jsonify(ModelSchema().dump(user_obj))
    # return Response("", status=201, mimetype='application/json')


@db_lifecycle
@session_lifecycle
def delete_obj_by_id(ModelSchema, Model, Id):
    obj = session.query(Model).filter_by(id=Id).first()
    session.delete(obj)
    return jsonify(ModelSchema().dump(obj))
