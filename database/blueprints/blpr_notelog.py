from database.models import user, note_log
from database.db_utils import *
from database.schemas import NoteLogSchema

from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/note_log', methods=["GET"])
def get_logs():
    return get_objects(NoteLogSchema, note_log)


@app.route("/note_log/<int:Id>", methods=["GET"])
@jwt_required()
def get_log_by_Id(Id):
    current_user_email = get_jwt_identity()
    user_obj = user.query.filter_by(email=current_user_email).first()
    note_obj = note_log.query.filter_by(id=Id).first()

    if note_obj.user_id != user_obj.id:
        return jsonify("Access denied", 402)
    return get_obj_by_Id(NoteLogSchema, note_log, Id)


@app.route("/note/note_log/<int:Id>", methods=["GET"])
@db_lifecycle
@session_lifecycle
def get_logs_by_Id(Id):
    logs = session.query(note_log).filter_by(note_id=Id)

    if logs.first() is None:
        raise InvalidUsage("Object not found", status_code=404)

    return jsonify(NoteLogSchema(many=True).dump(logs))