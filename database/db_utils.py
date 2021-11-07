from functools import wraps

from flask import jsonify

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


@session_lifecycle
def create_entry(model_class, **kwargs):
    entry = model_class(**kwargs)
    session.add(entry)
    return entry


def get_entries(model_class):  # GET entries by ids
    return model_class.query.all()


def get_entry_by_uid(model_class, obj_id):  # GET entry by id
    return model_class.query.get(obj_id)


def get_entry_by_username(model, username):  # GET entry by name
    return model.query.filter_by(username=username).first()


@session_lifecycle
def update_entry_by_uid(model, obj_id, **kwargs):  # PUT entity by id
    model = session.query(model).filter_by(id=obj_id).first()
    for key, value in kwargs.items():
        setattr(model, key, value)

    return model


@session_lifecycle
def delete_entry_by_id(model_class, obj_id):  # DELETE entity by id
    model = session.query(model_class).filter_by(id=obj_id).first()
    session.delete(model)
    return model
