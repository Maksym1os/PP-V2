from functools import wraps

import marshmallow
import sqlalchemy
from flask import jsonify, request

from database.flask_ini import app
from database.models import Session

session = Session()


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        # rv['status_code'] = self.status_code
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


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
            elif isinstance(e, marshmallow.exceptions.ValidationError):
                if str(e.args[0]).find("Unknown field") != -1:
                    raise InvalidUsage("Unknown field", status_code=400)
                elif str(e.args[0]).find("Not a valid") != -1:
                    raise InvalidUsage("Wrong type", status_code=400)
                raise e
            elif isinstance(e, sqlalchemy.exc.IntegrityError):
                if str(e.args[0]).find("Duplicate entry") != -1:
                    raise InvalidUsage("Duplicate entry", status_code=400)
                if str(e.args[0]).find("Cannot delete or update a parent row: a foreign key constraint fails") != -1:
                    raise InvalidUsage("Cannot delete or update this object", status_code=400)
                if str(e.args[0]).find("Cannot add or update a child row: a foreign key constraint fails") != -1:
                    raise InvalidUsage("Cannot add or update this object, incorrect data", status_code=400)
                else:
                    raise InvalidUsage("Incorrect data", status_code=400)
                # return str(e.args[0])
                # raise e
            else:
                # raise e
                raise InvalidUsage("InternalServerError", status_code=404)

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
    if obj is None:
        raise InvalidUsage("Object not found", status_code=404)
    return jsonify(ModelSchema().dump(obj))


@db_lifecycle
@session_lifecycle
def upd_obj_by_Id(ModelSchema, Model, Id):
    new_data = ModelSchema().load(request.get_json())
    obj = session.query(Model).filter_by(id=Id).first()
    if obj is None:
        raise InvalidUsage("Object not found", status_code=404)

    for key, value in new_data.items():
        setattr(obj, key, value)

    return jsonify(ModelSchema().dump(obj))
    # return Response("", status=201, mimetype='application/json')


@db_lifecycle
@session_lifecycle
def delete_obj_by_id(ModelSchema, Model, Id):
    obj = session.query(Model).filter_by(id=Id).first()

    if obj is None:
        raise InvalidUsage("Object not found", status_code=404)

    session.delete(obj)
    return jsonify(ModelSchema().dump(obj))
