from database.db_utils import *

from flask import request, jsonify


def create_obj(ModelSchema, Model):
    data = ModelSchema().load(request.get_json())
    obj = create_entry(Model, **data)

    return jsonify(ModelSchema().dump(obj))
    # return "", 200


def get_objects(ModelSchema, Model):
    users = get_entries(Model)
    return jsonify(ModelSchema(many=True).dump(users))


def get_obj_by_Id(ModelSchema, Model, Id):
    obj = get_entry_by_uid(Model, Id)
    return jsonify(ModelSchema().dump(obj))


def upd_obj_by_Id(ModelSchema, Model, Id):
    new_data = ModelSchema().load(request.get_json())
    user_obj = update_entry_by_uid(Model, Id, **new_data)

    return jsonify(ModelSchema().dump(user_obj))
    # return Response("", status=201, mimetype='application/json')


def delete_obj_by_id(ModelSchema, Model, Id):
    obj = delete_entry_by_id(Model, Id)
    return jsonify(ModelSchema().dump(obj))
