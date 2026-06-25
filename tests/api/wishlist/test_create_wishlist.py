def test_create_wishlist(wishlist_client, wishlist_data):
    response = wishlist_client.create(wishlist_data)
    assert response.status_code == 201
    json_data = response.json()
    assert "id" in json_data
