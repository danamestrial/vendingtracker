from flask import Flask
from flask.testing import FlaskClient
from routes.utils import select_query, status, value_query


def test_status() -> None:
    """Test status method."""
    assert status(True, "This is True") == {"status": True, "message": "This is True"}
    assert status(False, "This is False") == {
        "status": False,
        "message": "This is False",
    }


def test_select_query(client: FlaskClient, app: Flask) -> None:
    """Test select_query method."""
    with app.app_context():
        query_result = select_query("SELECT * FROM items")
        client_req = client.get("/item/list-all").json
        assert query_result == client_req

    with app.app_context():
        query_result = select_query("SELECT * FROM items WHERE id = %s", (1,))
        assert query_result["status"]

    with app.app_context():
        query_result = select_query("SELECT * FROM items WHERE id = %s", ())
        assert not query_result["status"]


def test_value_query(client: FlaskClient, app: Flask) -> None:
    """Test value_query method."""
    with app.app_context():
        query_result = value_query("insert into items(name) values(%s)", ("TEST_PASS",))
        assert query_result == status(True)
        query_result = value_query(
            "insert into items(name) values(%s)", ("TEST_FAIL", 999)
        )
        assert not query_result["status"]

    list_response = client.get("/item/list-all")
    item_list = list_response.json["message"]
    unique_id = list(filter(lambda x: x["name"] == "TEST_PASS", item_list))[0]["id"]

    with app.app_context():
        query_result = value_query("delete from items where id = %s", (int(unique_id),))
        assert query_result == status(True)
