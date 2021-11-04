from marshmallow import post_load, Schema, fields
from sql import user


class UserSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
