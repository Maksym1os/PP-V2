from sql import Session


def create_entry(model_class, **kwargs):
    obj = model_class(**kwargs)
    # with Session() as s:
    #     s.add(obj)
    return obj
