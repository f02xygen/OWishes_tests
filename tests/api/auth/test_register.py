import allure
import json
import pytest

negative_cases = [
    ({
        "email": "valid_email@example.com",
        "password": "12",
        "name": "test_name"
    }, 400),
    ({
        "email": "nonvalid_email@@example.com",
        "password": "Password123!",
        "name": "test_name"
    }, 422)
]

@allure.story("Auth")
@allure.title("Успешная регистрация нового пользователя")
def test_register(auth_client, user_data):
    with allure.step("Отправить POST на /api/auth/register"):
        response = auth_client.register(user_data)
    with allure.step("Проверить статус-код запроса"):
        assert response.status_code == 201
        allure.attach(name="response text", body=json.dumps(response.json()), 
                      attachment_type=allure.attachment_type.JSON)

@allure.story("Auth")
@allure.title("Невалидная регистрация пользователя")
@pytest.mark.parametrize("invalid_user_data, expected_status", negative_cases)                      
def test_register_negative(auth_client, invalid_user_data, expected_status):
    with allure.step("Отправить POST на /api/auth/register"):
        response = auth_client.register(invalid_user_data)
    with allure.step("Проверить статус-код запроса"):
        assert response.status_code == expected_status
        allure.attach(name="response text", body=json.dumps(response.json()), 
                      attachment_type=allure.attachment_type.JSON)