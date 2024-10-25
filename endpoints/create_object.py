import requests


class CreateObject:
    response = None
    response_json = None

    def new_object(self, payload):
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json['name'] == name, f'Wrong name, expected {name}, actual {self.response_json["name"]}'

    def check_response_code(self, resp_code):
        assert self.response.status_code == resp_code, (f'Wrong status code, expected {resp_code}, '
                                                        f'actual {self.response.status_code}')
