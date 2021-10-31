from marshmallow import Schema, fields


class UserRegister(Schema):
    id = fields.Str(required=False)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    email = fields.Email(required=True)


class UserAuth(Schema):
    usernameOrEmail = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
