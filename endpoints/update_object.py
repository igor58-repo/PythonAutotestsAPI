import requests


class UpdateObject:
    response = None
    response_json = None

    def update_object_by_id(self, obj_id, payload):
        self.response = requests.put(f"https://api.restful-api.dev/objects/{obj_id}", json=payload)
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json['name'] == name, f'Wrong name, expected {name}, actual {self.response_json["name"]}'

    def check_response_is_200(self):
        assert self.response.status_code == 200, f'Wrong status code, expected 200, actual {self.response.status_code}'