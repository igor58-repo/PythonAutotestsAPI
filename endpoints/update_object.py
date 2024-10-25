import requests


class UpdateObject:
    response = None
    response_json = None

    def update_object_by_id(self, obj_id, payload):
        self.response = requests.put(f"https://api.restful-api.dev/objects/{obj_id}", json=payload)
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json['name'] == name, f'Wrong name, expected {name}, actual {self.response_json["name"]}'

    def check_response_code(self, resp_code):
        assert self.response.status_code == resp_code, (f'Wrong status code, expected {resp_code}, '
                                                        f'actual {self.response.status_code}')
