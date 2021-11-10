from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    password = fields.String()
    email = fields.String()
    username = fields.String()
    phone = fields.Number()
    user_status = fields.Integer()


class NoteSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    name = fields.String()
    content = fields.String()
    tag = fields.String()


class NoteLogSchema(Schema):
    id = fields.Integer()
    note_id = fields.Integer()
    user_id = fields.Integer()
    action_id = fields.Integer()


