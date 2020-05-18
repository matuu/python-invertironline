from invertironline.http_handler import HttpHandler


class IOL:

    is_sandbox = True

    def __init__(self, http_handler_class, authentication_class, is_sandbox=True):
        self.is_sandbox = is_sandbox
        if is_sandbox:
            self._http_handler = http_handler_class('https://api-sandbox.invertironline.com')
        else:
            self._http_handler = http_handler_class('https://api.invertironline.com')
        self._authentication = authentication_class(self._http_handler)

    def _get(self, relative_url):
        return self._http_handler.get_request(
            relative_url,
            headers=self._authentication.build_auth_headers()
        )

    def _post(self, relative_url, body):
        return self._http_handler.post_request(
            relative_url,
            data=body,
            headers=self._authentication.build_auth_headers()
        )

    def login(self, username, password):
        return self._authentication.login(username, password)

    def refresh_token(self):
        return self._authentication.refresh_token()


    ########################################
    ####       PUBLIC IOL METHODS       ####
    ########################################


    def account_state(self):
        response = self._get("api/v2/estadocuenta")
        return response.json()
