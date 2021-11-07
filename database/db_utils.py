def create_entry(model_class, **kwargs):
    return model_class(**kwargs)


def get_entry_by_uid(model_class, obj_id):
    return model_class.query.get(obj_id)


def get_entry_by_username(model, username):
    return model.query.filter_by(username=username).first()


def update_entry_by_uid(model, session, obj_id, **kwargs):

    def update_model(self, **kwargs2):
        for key, value in kwargs2.items():
            setattr(self, key, value)

    update_model(session.query(model).filter_by(id=obj_id).first(), **kwargs)


