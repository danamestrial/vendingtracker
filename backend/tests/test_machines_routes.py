from flask.testing import FlaskClient


def test_list_all(client: FlaskClient) -> None:
    """To Test list-all machine endpoint."""
    response = client.get("/machine/list-all")
    assert response.status_code == 200
    response_json = response.json
    assert type(response_json["message"]) == list


def test_add_machine(client: FlaskClient) -> None:
    """To Test add machine endpoint."""
    args = {"handle": "TEST", "location": "TEST", "status": 1}
    response = client.post("/machine/add", query_string=args)
    assert response.status_code == 200
    json = response.json
    assert json["status"]
    assert json["message"] == ""


def test_update_machine(client: FlaskClient) -> None:
    """To Test update machine endpoint."""
    list_response = client.get("/machine/list-all")
    machine_list = list_response.json["message"]
    unique_id = list(filter(lambda x: x["handle"] == "TEST", machine_list))[0]["id"]
    args = {"handle": "NEWTEST", "location": "NEWTEST", "machine_id": unique_id}
    response = client.patch("/machine/update", query_string=args)
    assert response.status_code == 200
    response_json = response.json
    assert response_json["status"]
    assert response_json["message"] == ""


def test_delete_machine(client: FlaskClient) -> None:
    """To Test delete machine endpoint."""
    list_response = client.get("/machine/list-all")
    machine_list = list_response.json["message"]
    unique_id = list(filter(lambda x: x["handle"] == "NEWTEST", machine_list))[0]["id"]
    args = {"machine_id": unique_id}
    response = client.delete("/machine/delete", query_string=args)
    assert response.status_code == 200
    response_json = response.json
    assert response_json["status"]
    assert response_json["message"] == ""
