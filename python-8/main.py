import jwt


_SECRET = 'acelera'


def create_token(data, secret=_SECRET):
    return jwt.encode(data, secret, algorithm='HS256')


def verify_signature(token, secret=_SECRET):

    try:
        resp = jwt.decode(token, secret, algorithms=['HS256'])
    except jwt.InvalidTokenError:
        resp = {'error': 2}

    return resp
