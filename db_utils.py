from sql import Session


def create_entry(model_class, **kwargs):
    obj = model_class(**kwargs)
    # with Session() as s:
    #     s.add(obj)
    return obj


def get_entry_by_uid(model_class, obj_id):
    return model_class.query.get(obj_id)
