from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    id = fields.Integer()
    first_name = fields.String(validate=validate.Length(max=45))
    last_name = fields.String(validate=validate.Length(max=50))
    password = fields.String(validate=validate.Length(max=100))
    email = fields.String(validate=validate.Length(max=255))
    username = fields.String(validate=validate.Length(max=45))
    phone = fields.Number(validate=validate.Length(max=20))
    user_status = fields.Integer()


class NoteSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    name = fields.String(validate=validate.Length(max=255))


class NoteLogSchema(Schema):
    id = fields.Integer()
    note_id = fields.Integer()
    user_id = fields.Integer()
    action_id = fields.Integer()


