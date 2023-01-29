import requests
import os
from dotenv import load_dotenv
from secrets import token_urlsafe

load_dotenv()

host = os.getenv('HOST', '127.0.0.1')
port = os.getenv('PORT', '5000')
base_url = f"http://{host}:{port}"
rand_handle = token_urlsafe(16)
rand_handle_new = token_urlsafe(16)


def test_list_all():
    response = requests.get(f"{base_url}/item/list-all")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['status']
    assert type(response_json['message']) == list


def test_add_item():
    args = {"item_name": rand_handle}
    response = requests.post(f"{base_url}/item/add", params=args)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['status']
    assert response_json['message'] == ""


def test_update_item():
    list_response = requests.get(f"{base_url}/item/list-all")
    item_list = list_response.json()['message']
    unique_id = list(filter(lambda x: x["name"] == rand_handle, item_list))[0]['id']
    args = {"item_name": rand_handle_new, "item_id": unique_id}
    response = requests.patch(f"{base_url}/item/update", params=args)
    assert response.status_code == 200
    response_json = response.json()
    print(response_json)
    assert response_json['status']
    assert response_json['message'] == ""


def test_delete_item():
    list_response = requests.get(f"{base_url}/item/list-all")
    item_list = list_response.json()['message']
    unique_id = list(filter(lambda x: x["name"] == rand_handle_new, item_list))[0]['id']
    args = {"item_id": unique_id}
    response = requests.delete(f"{base_url}/item/delete", params=args)
    assert response.status_code == 200
    response_json = response.json()
    print(response_json)
    assert response_json['status']
    assert response_json['message'] == ""
