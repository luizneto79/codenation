from main import create_token, verify_signature
import jwt


class TestChallenge4:

    token = (b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsYW5ndWFnZSI6IlB5dGhvbi'
             b'J9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M')

    def test_create_token(self):
        assert create_token({"language": "Python"}, "acelera") == self.token


def test_verifica_assinatura_ok(monkeypatch):

    token = b'iLCJhbGciOiJIUzI1'

    def mock_jwt_decode(token, secret='acelera', algorithms=['HS256']):
        return {"language": "Python"}

    monkeypatch.setattr(jwt, 'decode', mock_jwt_decode)
    resp = verify_signature(token, 'acelera')

    assert (resp == {"language": "Python"})


def test_verifica_assinatura_exception_error(monkeypatch):

    token = b'iLCJhbGciOiJIUzI1'

    def mock_jwt_decode(token, secret='acelera', algorithms=['HS256']):
        return jwt.InvalidTokenError

    monkeypatch.setattr(jwt, 'decode', mock_jwt_decode)
    resp = verify_signature(token, 'acelera')

    assert (resp == jwt.InvalidTokenError)


def test_verifica_assinatura_reponse_error(monkeypatch):

    token = b'iLCJhbGciOiJIUzI1'

    def mock_jwt_decode(token=token, secret='acelera', algorithms=['HS256']):
        return {'error': 2}

    monkeypatch.setattr(jwt, 'decode', mock_jwt_decode)
    resp = verify_signature(token, 'acelera')

    assert (resp == {'error': 2})


