import allure
from faker import Faker
import pytest

fake = Faker()


negative_cases = [
    ({
        "title": "",
        "description": "test_desc",
        "event_date": fake.future_date().isoformat()
    }, 400),
    ({
        "title": "   ",
        "description": "test_desc",
        "event_date": fake.future_date().isoformat()
    }, 400),
    ({
        "title": "test_title",
        "description": "test_desc",
        "event_date": fake.past_date().isoformat()
    }, 400)
]

@allure.story("Wishlists")
@allure.title("Создание валидного вишлиста")
def test_create_wishlist(wishlist_client, wishlist_data):
    with allure.step("Отправить POST на /api/wishlists/"):
        response = wishlist_client.create(wishlist_data)
    with allure.step("Проверить статус-код ответа"):
        assert response.status_code == 201
    with allure.step("Проверить наличие поля id в ответе сервера"):
        json_data = response.json()
        assert "id" in json_data

@allure.story("Wishlists")
@allure.title("Создание невалидного вишлиста")
@pytest.mark.parametrize("invalid_wishlist_data, expected_status", negative_cases)   
def test_create_wishlist_negative(wishlist_client, invalid_wishlist_data, expected_status):
    with allure.step("Отправить POST на /api/wishlists/"):
        response = wishlist_client.create(invalid_wishlist_data)
    with allure.step("Проверить статус-код ответа"):
        assert response.status_code == expected_status