import requests
import pytest

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

def test_single_object(obj_id):
    id = obj_id['id']
    response = requests.get(f'https://api.restful-api.dev/objects/{id}')
    response_json = response.json()
    assert response.status_code == 200, f'Wrong status code, expected 200, actual {response.status_code}'
    assert response_json['name'] == payload['name'], f'Wrong name, expected {payload["name"]}, actual {response_json["name"]}'


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
    id = obj_id['id']
    response = requests.put(f'https://api.restful-api.dev/objects/{id}', json=new_payload)
    response_json = response.json()
    assert response.status_code == 200, f'Wrong status code, expected 200, actual {response.status_code}'
    assert response_json['name'] == new_payload['name'], f'Wrong name, expected {new_payload["name"]}, actual {response_json["name"]}'


def test_delete_object(obj_id):
    id = obj_id['id']
    delete_response = requests.delete(f'https://api.restful-api.dev/objects/{id}')
    get_response = requests.get(f'https://api.restful-api.dev/objects/{id}')
    assert delete_response.status_code == 200, f'Wrong status code, expected 200, actual {delete_response.status_code}'
    assert get_response.status_code == 404, f'Wrong status code, expected 404, actual {delete_response.status_code}'
