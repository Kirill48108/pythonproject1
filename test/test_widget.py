import pytest

from src.widget import mask_account_card, get_date


@pytest.fixture
def card_masks():
    return "MasterCard 1234567890123456"


def test_mask_account_card(card_masks):
    assert mask_account_card(card_masks) == "MasterCard 1234 56** **** 3456"


@pytest.fixture
def bank_masks():
    return "Счет 12345678901234567893"


def test_mask_account_card_1(bank_masks):
    assert mask_account_card(bank_masks) == "Счет **7893"


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
        ("Visa Gold A 1234567890123456", "Visa Gold A 1234 56** **** 3456"),
        ("Счет 12345678901234567893", "Счет **7893"),
        ("Счёт 12345678901234567893", "Счёт **7893"),
        ("VisaGold1234567890123456", "Ошибка в введённых данных!"),
        ("Счет12345678901234567893", "Ошибка в введённых данных!"),
        ("Visa Gold A 123456789012345v", "Некорректный ввод."),
        ("Счет 1234567890123456789", "Некорректный ввод."),
    ],
)
def test_mask_account_card_2(numbers, expected):
    assert mask_account_card(numbers) == expected


@pytest.mark.parametrize(
    "incorrect_date, expected",
    [
        ("2024-03-11T02:26:18.6714070", "Вы ввели неверный формат входных данных"),
        ("", "Вы ввели неверный формат входных данных"),
        ("2024-03-00T02:26:18.671407", "День указан неверно"),
        ("2024-03-32T02:26:18.671407", "День указан неверно"),
        ("2024-00-11T02:26:18.671407", "Месяц указан неверно"),
        ("2024-13-11T02:26:18.671407", "Месяц указан неверно"),
        ("0000-03-11T02:26:18.671407", "Год указан неверно"),
        ("9001-03-11T02:26:18.671407", "Год указан неверно"),
    ],
)
def test_get_date_invalid_date(incorrect_date, expected):
    with pytest.raises(ValueError) as exc_info:
        get_date(incorrect_date)
    assert str(exc_info.value) == expected
