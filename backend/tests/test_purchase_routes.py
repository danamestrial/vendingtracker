from flask.testing import FlaskClient


def test_vending_machine_records(client: FlaskClient) -> None:
    """Test machine records."""
    response = client.get("/item/records")
    assert response.status_code == 200
    response_json = response.json
    assert response_json["status"]


def test_product_records(client: FlaskClient) -> None:
    """Test item records."""
    response = client.get("/machine/records")
    assert response.status_code == 200
    response_json = response.json
    assert response_json["status"]
