import requests
import os
from dotenv import load_dotenv
from secrets import token_urlsafe

load_dotenv()

host = os.getenv('HOST', '127.0.0.1')
port = os.getenv('PORT', '5000')
base_url = f"http://{host}:{port}"
rand_dict = {"handle": token_urlsafe(16), "location": token_urlsafe(16)}
rand_dict_new = {"handle": token_urlsafe(16), "location": token_urlsafe(16)}


def test_list_all():
    response = requests.get(f"{base_url}/machine/list-all")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['status']
    assert type(response_json['message']) == list


def test_add_machine():
    args = {"handle": rand_dict["handle"], "location": rand_dict["location"], "status": 1}
    response = requests.post(f"{base_url}/machine/add", params=args)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['status']
    assert response_json['message'] == ""


def test_update_machine():
    list_response = requests.get(f"{base_url}/machine/list-all")
    machine_list = list_response.json()['message']
    unique_id = list(filter(lambda x: x["handle"] == rand_dict["handle"], machine_list))[0]['id']
    args = {"handle": rand_dict_new["handle"], "location": rand_dict_new["location"], "machine_id": unique_id}
    response = requests.patch(f"{base_url}/machine/update", params=args)
    assert response.status_code == 200
    response_json = response.json()
    print(response_json)
    assert response_json['status']
    assert response_json['message'] == ""


def test_delete_machine():
    list_response = requests.get(f"{base_url}/machine/list-all")
    machine_list = list_response.json()['message']
    unique_id = list(filter(lambda x: x["handle"] == rand_dict_new["handle"], machine_list))[0]['id']
    args = {"machine_id": int(unique_id)}
    response = requests.delete(f"{base_url}/machine/delete", params=args)
    assert response.status_code == 200
    response_json = response.json()
    print(response_json)
    assert response_json['status']
    assert response_json['message'] == ""
