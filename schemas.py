from marshmallow import post_load, Schema, fields
from sql import user

#
# class UserData(Schema):
#     class Meta:
#         fields = ("id", "username")


class UserSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()

    # @post_load
    # def make_user(self, data):
    #     return user(**data)
