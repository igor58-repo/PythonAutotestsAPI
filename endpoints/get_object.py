import requests
from endpoints.base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):
    response = None
    response_json = None

    def get_object_by_id(self, obj_id):
        self.response = requests.get(f"https://api.restful-api.dev/objects/{obj_id}")
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json['name'] == name, f'Wrong name, expected {name}, actual {self.response_json["name"]}'
