def test_create_item(item_client, created_wid, item_data):
    response = item_client.create(created_wid, item_data)
    assert response.status_code == 201
