from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject

payload = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}

new_payload = {
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2024,
            "price": 2849.99,
            "CPU model": "M10",
            "Hard disk size": "1 TB"
        }
    }


def test_create_object():
    new_object_endpoint = CreateObject()
    new_object_endpoint.new_object(payload)
    new_object_endpoint.check_response_code(200)
    new_object_endpoint.check_name(payload['name'])


def test_get_object(obj_id):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_object_by_id(obj_id['id'])
    get_object_endpoint.check_response_code(200)
    get_object_endpoint.check_name(payload['name'])


def test_update_object(obj_id):
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_object_by_id(obj_id['id'], new_payload)
    update_object_endpoint.check_response_code(200)
    update_object_endpoint.check_name(new_payload['name'])


def test_delete_object(obj_id):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_object_by_id(obj_id['id'])
    delete_object_endpoint.check_response_code(200)
    get_object_endpoint = GetObject()
    get_object_endpoint.get_object_by_id(obj_id['id'])
    get_object_endpoint.check_response_code(404)

