from flask.testing import FlaskClient


def test_list_all(client: FlaskClient) -> None:
    """To Test list-all item endpoint."""
    response = client.get("/item/list-all")
    assert response.status_code == 200
    response_json = response.json
    assert response_json["status"]
    assert type(response_json["message"]) == list


def test_add_item(client: FlaskClient) -> None:
    """To Test add item endpoint."""
    args = {"item_name": "TEST_ITEM"}
    response = client.post("/item/add", query_string=args)
    assert response.status_code == 200
    response_json = response.json
    assert response_json["status"]
    assert response_json["message"] == ""


def test_update_item(client: FlaskClient) -> None:
    """To Test update item endpoint."""
    list_response = client.get("/item/list-all")
    item_list = list_response.json["message"]
    unique_id = list(filter(lambda x: x["name"] == "TEST_ITEM", item_list))[0]["id"]
    args = {"item_name": "NEW_TEST_ITEM", "item_id": unique_id}
    response = client.patch("/item/update", query_string=args)
    assert response.status_code == 200
    response_json = response.json
    assert response_json["status"]
    assert response_json["message"] == ""


def test_delete_item(client: FlaskClient) -> None:
    """To Test delete item endpoint."""
    list_response = client.get("/item/list-all")
    item_list = list_response.json["message"]
    unique_id = list(filter(lambda x: x["name"] == "NEW_TEST_ITEM", item_list))[0]["id"]
    args = {"item_id": unique_id}
    response = client.delete("/item/delete", query_string=args)
    assert response.status_code == 200
    response_json = response.json
    assert response_json["status"]
    assert response_json["message"] == ""
