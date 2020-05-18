import requests


class HttpHandler:
    session = None
    base_url_api = None

    def __init__(self, base_url_api):
        self.base_url_api = base_url_api
        self.session = requests.Session()

    def get_request(self, url, headers=None):
        return self.session.get(f"{self.base_url_api}/{url}", headers=headers)

    def post_request(self, url, data, headers=None):
        return self.session.post(f"{self.base_url_api}/{url}", data=data, headers=headers)
