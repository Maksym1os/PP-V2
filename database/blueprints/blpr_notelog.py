from database.flask_ini import app

from database.models import note_log

from database.db_utils import *

from database.schemas import NoteLogSchema


@app.route('/note_log', methods=["GET"])
def get_logs():
    return get_objects(NoteLogSchema, note_log)


@app.route("/note_log/<int:Id>", methods=["GET"])
def get_log_by_Id(Id):
    return get_obj_by_Id(NoteLogSchema, note_log, Id)


@app.route("/note/note_log/<int:Id>", methods=["GET"])
@db_lifecycle
@session_lifecycle
def get_logs_by_Id(Id):
    logs = session.query(note_log).filter_by(note_id=Id)

    if logs.first() is None:
        raise InvalidUsage("Object not found", status_code=404)

    return jsonify(NoteLogSchema(many=True).dump(logs))