def create_entry(model_class, **kwargs):
    return model_class(**kwargs)


def get_entry_by_uid(model_class, obj_id):
    return model_class.query.get(obj_id)


def update_entry_by_uid(self, **kwargs):
    for key, value in kwargs.items():
        setattr(self, key, value)
