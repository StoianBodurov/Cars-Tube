from functools import wraps
from flask import request
from werkzeug.exceptions import BadRequest


def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            schema = schema_name()
            errors = schema.validate(request.get_json())
            if errors:
                raise BadRequest(f'Invalid fields {errors}')
            return f(*args, **kwargs)
        return wrapper
    return decorator
