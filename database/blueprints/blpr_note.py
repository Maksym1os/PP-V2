from database.flask_ini import app

from database.models import note, note_log, action

from database.db_utils import *

from database.schemas import NoteSchema


@app.route("/note", methods=["POST"])
@db_lifecycle
@session_lifecycle
def create_note():
    data = NoteSchema().load(request.get_json())
    obj = note(**data)

    act = action("created note")
    log = note_log(obj.id, 1, act.id)
    session.add(act)
    session.add(log)
    session.add(obj)

    return jsonify(NoteSchema().dump(obj))


@app.route('/note', methods=["GET"])
def get_notes():
    return get_objects(NoteSchema, note)


@app.route("/note/<int:Id>", methods=["GET"])
def get_note_by_Id(Id):
    return get_obj_by_Id(NoteSchema, note, Id)


@app.route("/note/<int:Id>", methods=["PUT"])
@db_lifecycle
@session_lifecycle
def upd_note_by_Id(Id):
    new_data = NoteSchema().load(request.get_json())
    obj = session.query(note).filter_by(id=Id).first()
    act = action(obj.name)
    log = note_log(obj.id, 1, act.id)

    session.add(log)

    if obj is None:
        raise InvalidUsage("Object not found", status_code=404)

    for key, value in new_data.items():
        setattr(note, key, value)

    return jsonify(NoteSchema().dump(obj))


@app.route("/note/<int:Id>", methods=["DELETE"])
def delete_note_by_id(Id):
    return delete_obj_by_id(NoteSchema, note, Id)
