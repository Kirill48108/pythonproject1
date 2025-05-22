import pytest


@pytest.fixture
def correct_date():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def not_correct_data():
    return [{"date": "12-03-18"}]


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 970157810,
            "date": "2018-06-08T10:3:58.027767",
            "operationAmount": {"amount": "150", "currency": {"code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет - 63475662387234505765",
            "to": "Счет 8175128657841941437",
        }
    ]
