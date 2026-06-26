import allure

@allure.title("Создание валидного вишлиста")
def test_create_wishlist(wishlist_client, wishlist_data):
    with allure.step("Отправить POST на /api/wishlists/"):
        response = wishlist_client.create(wishlist_data)
    with allure.step("Проверить статус-код ответа"):
        assert response.status_code == 201
    with allure.step("Проверить наличие поля id в ответе сервера"):
        json_data = response.json()
        assert "id" in json_data
