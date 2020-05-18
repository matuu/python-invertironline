class IolAuthentication:
    token = None
    token_response = None

    def __init__(self, http_handler):
        self._http_handler = http_handler

    def build_auth_headers(self, **kwargs):
        _auth_headers = dict(Authorization=f"Bearer {self.token}")
        _auth_headers.update(kwargs)
        return _auth_headers


    def login(self, username, password):
        self.username = username
        self.password = password
        return self._retrieve_token(
            dict(
                username=self.username,
                password=self.password,
                grant_type='password'
            )
        )

    def refresh_token(self):
        return self._retrieve_token(body=dict(
            refresh_token=self.token_response.get('refresh_token'),
            grant_type='refresh_token'
            ))

    def _retrieve_token(self, body):
        response = self._http_handler.post_request("token", data=body)
        self.token_response = response.json()
        self.token = self.token_response.get('access_token')
        return self.token
