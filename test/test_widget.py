import pytest

from src.widget import get_date, mask_account_card


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


@pytest.mark.parametrize(
    "nums,expected",
    [
        ("Visa 7000792289606361", "Visa 7000 79** **** 6361"),
        ("Счётytuuikuokyyiuyuuyk", "Некорректный ввод."),
        ("Счёт 12345678876543211234", "Счёт **1234"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("", "Некорректный ввод."),
        ("Maestro 5456789645321234", "Maestro 5456 78** **** 1234"),
        ("Maestro67444444474", "Некорректный ввод."),
        ("MasterCard35575737", "Некорректный ввод."),
        ("Visa7765785688558", "Некорректный ввод."),
    ],
)
def test_mask_account_card(nums, expected):
    assert mask_account_card(nums) == expected
