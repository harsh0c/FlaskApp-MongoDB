from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.String()
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
