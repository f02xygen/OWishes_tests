import allure

@allure.story("Item")
@allure.title("Создание валидного товара")
def test_create_item(item_client, created_wid, item_data):
    with allure.step(r"Отправить POST на /api/wishlists/{wishlist_id}/items/"):
        response = item_client.create(created_wid, item_data)
    with allure.step("Проверить статус-код запроса"):
        assert response.status_code == 201
