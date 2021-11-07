from database.flask_ini import app

from database.models import note

from database.db_utils import *

from database.schemas import NoteSchema


@app.route("/note", methods=["POST"])
def create_note():
    return create_obj(NoteSchema, note)


@app.route('/note', methods=["GET"])
def get_notes():
    return get_objects(NoteSchema, note)


@app.route("/user/<int:Id>", methods=["GET"])
def get_note_by_Id(Id):
    return get_obj_by_Id(NoteSchema, note, Id)


@app.route("/user/<int:Id>", methods=["PUT"])
def upd_note_by_Id(Id):
    return upd_obj_by_Id(NoteSchema, note, Id)


@app.route("/user/<int:Id>", methods=["DELETE"])
def delete_note_by_id(Id):
    return delete_obj_by_id(NoteSchema, note, Id)
