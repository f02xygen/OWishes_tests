import allure

@allure.story("Reservations")
@allure.title("Успешно зарезервировать товар")
def test_create_item(reservation_client, created_item_id, reservation_data):
    with allure.step("Отправить POST на /api/reservations/"):
        response = reservation_client.create(created_item_id, reservation_data)
    with allure.step("Проверить статус-код ответа"):
        assert response.status_code == 201
