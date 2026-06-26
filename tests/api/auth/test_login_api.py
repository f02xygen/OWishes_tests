import allure

@allure.story("Auth")
@allure.title("Успешный логин пользователя")
def test_login(auth_client, user_data):
    with allure.step("Зарегестрировать нового пользователя"):
        auth_client.register(user_data)
    with allure.step("Отправить POST на /api/auth/login"):
        response = auth_client.login(user_data["email"], user_data["password"])
    with allure.step("Проверить статус-код запроса"):
        assert response.status_code == 200
