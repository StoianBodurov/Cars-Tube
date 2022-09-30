from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import Unauthorized


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {'sub': user.id, 'exp': datetime.utcnow() + timedelta(days=2)}
        return jwt.encode(payload, key=config('SECRET_KEY'), algorithm='HS256')

    @staticmethod
    def decode_token(token):
        try:
            return jwt.decode(jwt=token, key=config('SECRET_KEY'), algorithms=['HS256'])
        except Exception as ex:
            raise ex


auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    try:
        return AuthManager.decode_token(token)
    except Exception:
        raise Unauthorized('Invalid or missing Token')


