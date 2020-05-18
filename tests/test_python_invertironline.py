from invertironline import __version__, IOL
from invertironline.authtentication import IolAuthentication
from invertironline.http_handler import HttpHandler


def test_version():
    assert __version__ == '0.1.0'


def test_sandbox_selection():
    iol_api = IOL(HttpHandler, IolAuthentication)

    assert iol_api.is_sandbox == True

    iol_api = IOL(HttpHandler, IolAuthentication, is_sandbox=False)
    assert iol_api.is_sandbox == False


def test_url_selection():
    iol_api = IOL(HttpHandler, IolAuthentication)
    assert iol_api._http_handler.base_url_api == 'https://api-sandbox.invertironline.com'

    iol_api = IOL(HttpHandler, IolAuthentication, is_sandbox=False)
    assert iol_api._http_handler.base_url_api == 'https://api.invertironline.com'
