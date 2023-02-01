def test_list_stocks(client):
    args = {"machine_id": 3}
    response = client.get("/stock/list", query_string=args)
    assert response.status_code == 200
    response_json = response.json
    assert response_json['status']
    assert type(response_json['message']) == list


def test_add_stock(client):
    args = {"machine_id": 3, "item_id": 1, "quantity": 5}
    response = client.post("/stock/add", query_string=args)
    assert response.status_code == 200
    response_json = response.json
    assert response_json['status']
    assert response_json['message'] == ""


def test_update_stock(client):
    args = {"machine_id": 3, "item_id": 1, "quantity": 7}
    response = client.patch("/stock/update", query_string=args)
    assert response.status_code == 200
    response_json = response.json
    assert response_json['status']
    assert response_json['message'] == ""


def test_delete_stock(client):
    args = {"machine_id": 3, "item_id": 1}
    response = client.delete("/stock/delete", query_string=args)
    assert response.status_code == 200
    response_json = response.json
    assert response_json['status']
    assert response_json['message'] == ""
