class BaseEndpoint:
    response = None
    response_json = None

    def check_response_code(self, resp_code):
        assert self.response.status_code == resp_code, (f'Wrong status code, expected {resp_code}, '
                                                        f'actual {self.response.status_code}')
