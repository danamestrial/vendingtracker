from flask.testing import FlaskClient


def test_vending_machine_records(client: FlaskClient) -> None:
    response = client.get("/item/records")
    assert response.status_code == 200
    json = response.json
    assert json['status']


def test_product_records(client: FlaskClient) -> None:
    response = client.get("/machine/records")
    assert response.status_code == 200
    json = response.json
    assert json['status']


