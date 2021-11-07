from functools import wraps

from database.models import Session

session = Session()


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


def get_entry_by_uid(model_class, obj_id):
    return model_class.query.get(obj_id)


def get_entry_by_username(model, username):
    return model.query.filter_by(username=username).first()


@session_lifecycle
def update_entry_by_uid(model, obj_id, **kwargs):
    def update_model(self, **kwargs2):
        for key, value in kwargs2.items():
            setattr(self, key, value)

    update_model(session.query(model).filter_by(id=obj_id).first(), **kwargs)

    # return model.query.get(obj_id)
