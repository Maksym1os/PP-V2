from marshmallow import Schema, fields


class UserData(Schema):
    class Meta:
        fields = ("id", "username")


class UserToCreate(Schema):
    id = fields.Integer
    username = fields.String
