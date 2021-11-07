from database.flask_ini import app

from database.models import note_log

from database.db_utils import *

from database.schemas import NoteLogSchema


@app.route("/note_log", methods=["POST"])
def create_log():
    return create_obj(NoteLogSchema, note_log)


@app.route('/note_log', methods=["GET"])
def get_logs():
    return get_objects(NoteLogSchema, note_log)


@app.route("/note_log/<int:Id>", methods=["GET"])
def get_log_by_Id(Id):
    return get_obj_by_Id(NoteLogSchema, note_log, Id)


@app.route("/note_log/<int:Id>", methods=["PUT"])
def upd_log_by_Id(Id):
    return upd_obj_by_Id(NoteLogSchema, note_log, Id)
