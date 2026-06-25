def test_create_item(reservation_client, created_item_id, reservation_data):
    response = reservation_client.create(created_item_id, reservation_data)
    assert response.status_code == 201
