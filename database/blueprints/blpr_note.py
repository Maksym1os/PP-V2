from sqlalchemy import func

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
    act = action(name="created note")

    if request.json.get("user_id", None) is None:
        raise InvalidUsage("user_id is not present", status_code=400)

    session.add(act)
    session.add(obj)
    session.flush()

    log = note_log(obj.id, request.json.get("user_id", None), act.id)

    session.add(log)

    return jsonify(NoteSchema().dump(obj))


@app.route('/note', methods=["GET"])
def get_notes():
    return get_objects(NoteSchema, note)


@app.route("/note/<int:Id>", methods=["GET"])
def get_note_by_Id(Id):
    return get_obj_by_Id(NoteSchema, note, Id)


@app.route("/note/<string:tag>", methods=["GET"])
def get_notes_by_tag(tag):
    notes = note.query.filter_by(tag=tag).all()
    return jsonify(NoteSchema(many=True).dump(notes))


@app.route("/note/<int:Id>", methods=["PUT"])
@db_lifecycle
@session_lifecycle
def upd_note_by_Id(Id):
    new_data = NoteSchema().load(request.get_json())

    if request.json.get("user_id", None) is None:
        raise InvalidUsage("user_id not present", status_code=404)

    if session.query(note_log).filter_by(user_id=request.json.get("user_id", None)).first() is None:
        if session.query(note_log).filter_by(note_id=Id).distinct("user_id").count() > 4:
            raise InvalidUsage("More than 5 users", status_code=400)

    obj = session.query(note).filter_by(id=Id).first()

    if obj is None:
        raise InvalidUsage("Object not found", status_code=404)

    act = action(obj.name, obj.content)

    session.add(act)
    session.flush()

    log = note_log(obj.id, request.json.get("user_id", None), act.id)

    session.add(log)

    for key, value in new_data.items():
        setattr(obj, key, value)

    return jsonify(NoteSchema().dump(obj))


@app.route("/note/<int:Id>", methods=["DELETE"])
def delete_note_by_id(Id):
    return delete_obj_by_id(NoteSchema, note, Id)
