import requests
import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
payload = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}


@pytest.fixture()
def obj_id():
    response = requests.post('https://api.restful-api.dev/objects', json=payload)
    response_json = response.json()
    yield response_json
    requests.delete(f'https://api.restful-api.dev/objects/{response_json["id"]}')


def test_create_object():
    new_object_endpoint = CreateObject()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    new_object_endpoint.new_object(payload)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_name(payload['name'])


def test_get_object(obj_id):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_object_by_id(obj_id['id'])
    get_object_endpoint.check_response_is_200()
    get_object_endpoint.check_name(payload['name'])


def test_update_object(obj_id):
    new_payload = {
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2024,
            "price": 2849.99,
            "CPU model": "M10",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.put(f"https://api.restful-api.dev/objects/{obj_id['id']}", json=new_payload)
    response_json = response.json()
    assert response.status_code == 200, f'Wrong status code, expected 200, actual {response.status_code}'
    assert response_json['name'] == new_payload[
        'name'], f'Wrong name, expected {new_payload["name"]}, actual {response_json["name"]}'


def test_delete_object(obj_id):
    delete_response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id['id']}")
    get_response = requests.get(f"https://api.restful-api.dev/objects/{obj_id['id']}")
    assert delete_response.status_code == 200, f'Wrong status code, expected 200, actual {delete_response.status_code}'
    assert get_response.status_code == 404, f'Wrong status code, expected 404, actual {delete_response.status_code}'
