from marshmallow import  Schema, fields


class UserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)


class RequestRegisterUserSchema(UserSchema):
    first_name = fields.String(min_length=3, max_length=30, required=True)
    last_name = fields.String(min_length=3, max_length=30, required=True)


class RequestLoginUserSchema(UserSchema):
    pass
