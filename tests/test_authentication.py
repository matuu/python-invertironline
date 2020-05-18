from unittest.mock import Mock

from invertironline.authtentication import IolAuthentication
from invertironline.http_handler import HttpHandler


def test_auth_init():
    auth_instance = IolAuthentication(HttpHandler('http://testserver'))

    assert auth_instance._http_handler is not None


def test_login():
    http_handler_mock = Mock(spec=HttpHandler)
    auth_instance = IolAuthentication(http_handler_mock)

    # TODO: lamar a login y comprobar que se llama a con los parámetros correctos
