from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()


class NoteSchema(Schema):
    id = fields.Integer()
    name = fields.String()


class NoteLogSchema(Schema):
    id = fields.Integer()
    note_id = fields.Integer()
