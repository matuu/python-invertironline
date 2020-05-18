from unittest.mock import Mock

from invertironline.http_handler import HttpHandler


def test_init_instance():
    instance = HttpHandler('http://testserver')

    assert instance.base_url_api == 'http://testserver'


def test_get_request():
    instance = HttpHandler('http://testserver')
    instance.session = Mock()

    instance.get_request('test1')

    instance.session.get.assert_called_once_with(
        "http://testserver/test1",
        headers=None)


def test_get_request_with_extra_headers():
    instance = HttpHandler('http://testserver')
    instance.session = Mock()

    instance.get_request('test2', headers=dict(Extra='a_new_value'))

    instance.session.get.assert_called_once_with(
        "http://testserver/test2",
        headers=dict(Extra='a_new_value'))


def test_post_request():
    instance = HttpHandler('http://testserver')
    instance.session = Mock()

    instance.post_request('profile', dict(name='Joe'))

    instance.session.post.assert_called_once_with(
        "http://testserver/profile",
        data=dict(name='Joe'),
        headers=None)


def test_post_request_with_headers():
    instance = HttpHandler('http://testserver')
    instance.session = Mock()

    instance.post_request('profile', dict(name='Joe'), headers=dict(extra=1))

    instance.session.post.assert_called_once_with(
        "http://testserver/profile",
        data=dict(name='Joe'),
        headers=dict(extra=1))
