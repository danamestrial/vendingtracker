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


def test_list_stocks():
    args = {"machine_id": 3}
    response = requests.get(f"{base_url}/stock/list", params=args)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['status']
    assert type(response_json['message']) == list


def test_add_stock():
    args = {"machine_id": 3, "item_id": 1, "quantity": 5}
    response = requests.post(f"{base_url}/stock/add", params=args)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['status']
    assert response_json['message'] == ""


def test_update_stock():
    args = {"machine_id": 3, "item_id": 1, "quantity": 7}
    response = requests.patch(f"{base_url}/stock/update", params=args)
    assert response.status_code == 200
    response_json = response.json()
    print(response_json)
    assert response_json['status']
    assert response_json['message'] == ""


def test_delete_stock():
    args = {"machine_id": 3, "item_id": 1}
    response = requests.delete(f"{base_url}/stock/delete", params=args)
    assert response.status_code == 200
    response_json = response.json()
    print(response_json)
    assert response_json['status']
    assert response_json['message'] == ""
