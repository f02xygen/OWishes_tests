import pytest
from faker import Faker

fake = Faker()


@pytest.fixture
def user_data():
    return {
        "email": fake.email(),
        "name": fake.first_name(),
        "password": "Password123!",
    }

@pytest.fixture
def wishlist_data():
    return {
        "title": "test_title",
        "description": "test_description",
        "event_date": fake.future_date().isoformat()
    }

@pytest.fixture
def item_data():
    return {
        "title": "test_title",
        "url": fake.url(),
        "price": fake.random_number(digits=4),
        "priority": "low",
        "note": "test_note"
    }

@pytest.fixture
def reservation_data():
    return {
        "item_id": "",
        "reserver_name": fake.first_name(),
        "reserver_email": fake.email()
    }