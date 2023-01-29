import requests
import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('HOST', '127.0.0.1')
port = os.getenv('PORT', '5000')


def test_list_all():
    response = requests.get(f"http://{base_url}:{port}/machine/list-all")
    response_json = response.json()
    assert response_json['status']

