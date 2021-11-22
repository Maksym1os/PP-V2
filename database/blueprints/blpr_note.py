from database.models import note, note_log, user, action, connected_user
from database.db_utils import *
from database.schemas import NoteSchema

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


@app.route("/note", methods=["POST"])
@jwt_required()
@db_lifecycle
@session_lifecycle
def create_note():
    data = NoteSchema().load(request.get_json())
    obj = note(**data)
    act = action(name="created note")

    user_id = request.json.get("user_id", None)


    if user_id is None:
        raise InvalidUsage("user_id is not present", status_code=400)

    user_obj = user.query.filter_by(id=user_id).first()
    current_user_email = get_jwt_identity()

    if current_user_email != user_obj.email:
        return jsonify("Access denied", 402)

    session.add(act)
    session.add(obj)
    session.flush()

    log = note_log(obj.id, request.json.get("user_id", None), act.id)

    cu = connected_user(user_id=user_id, note_id=obj.id)
    session.add(cu)
    session.add(log)

    return jsonify(NoteSchema().dump(obj))


@app.route('/note/add/<int:input_user_id>,<int:input_note_id>', methods=["PUT"])
@jwt_required()
@db_lifecycle
@session_lifecycle
def add_user(input_user_id, input_note_id):
    current_user_email = get_jwt_identity()
    user_obj = user.query.filter_by(email=current_user_email).first()
    note_obj = note.query.filter_by(id=input_note_id).first()

    if user_obj.id != note_obj.user_id:
        return jsonify("Access denied", 402)

    cu = connected_user(user_id=input_user_id, note_id=input_note_id)
    session.add(cu)
    return jsonify("User added")

@app.route('/note', methods=["GET"])
def get_notes():
    return get_objects(NoteSchema, note)


@app.route("/note/<int:Id>", methods=["GET"])
@jwt_required()
@db_lifecycle
def get_note_by_Id(Id):
    current_user_email = get_jwt_identity()
    user_obj = user.query.filter_by(email=current_user_email).first()

    for cu in connected_user.query.all():
        if cu.note_id == Id and user_obj.id == cu.user_id:
            return get_obj_by_Id(NoteSchema, note, Id)

    return jsonify("Access denied", 402)


@app.route("/note/<string:tag>", methods=["GET"])
def get_notes_by_tag(tag):
    notes = note.query.filter_by(tag=tag).all()
    return jsonify(NoteSchema(many=True).dump(notes))


@app.route("/note/<int:Id>", methods=["PUT"])
@db_lifecycle
@session_lifecycle
@jwt_required()
def upd_note_by_Id(Id):
    current_user_email = get_jwt_identity()
    user_obj = user.query.filter_by(email=current_user_email).first()

    check = False

    for cu in connected_user.query.all():
        if cu.note_id == Id and user_obj.id == cu.user_id:
            check = True

    if not check:
        return jsonify("Access denied", 402)

    new_data = NoteSchema().load(request.get_json())

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
@db_lifecycle
@session_lifecycle
@jwt_required()
def delete_note_by_id(Id):
    current_user_email = get_jwt_identity()
    user_obj = user.query.filter_by(email=current_user_email).first()
    note_obj = note.query.filter_by(id=Id).first()

    if note_obj.user_id != user_obj.id:
        return jsonify("Access denied", 402)

    session2 = Session()
    for cu in connected_user.query.all():
        if cu.note_id == Id:
            session2.delete(cu)
    session2.commit()
    return delete_obj_by_id(NoteSchema, note, Id)
