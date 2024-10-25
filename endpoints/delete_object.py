import requests
from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    response = None
    response_json = None

    def delete_object_by_id(self, obj_id):
        self.response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
        self.response_json = self.response.json()

    def check_response_id(self, obj_id):
        actual_response_id = self.response_json['id']
        assert actual_response_id == obj_id, f'Wrong obj_id, expected {obj_id}, actual {actual_response_id}'
