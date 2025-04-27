import pytest

@pytest.fixture
def correct_date():
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def correct_date():
    return "2024-03-11T02:26:18.671407"

@pytest.fixture()
def test_get_date(correct_date):
    assert get_date(correct_date) == "11.03.2024"

@pytest.fixture
def not_correct_data():
    return [{'date': '12-03-18'}]
