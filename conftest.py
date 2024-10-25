import pytest
from endpoints.create_object import CreateObject
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


@pytest.fixture()
def obj_id():
    create_object = CreateObject()
    create_object.new_object(payload)
    yield create_object.response_json
    delete_object = DeleteObject()
    delete_object.delete_object_by_id(create_object.response_json['id'])
