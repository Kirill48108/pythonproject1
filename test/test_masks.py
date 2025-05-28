import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "numb_card, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("46894085699", "Некорректный ввод."),
        ("678594853758465784269", "Некорректный ввод."),
        ("6785948537584657842", "Некорректный ввод."),
        ("", "Некорректный ввод."),
        ("458345gfg893048", "Некорректный ввод."),
    ],
)
def test_mask_card_number_normal(numb_card, expected):
    assert get_mask_card_number(numb_card) == expected


@pytest.mark.parametrize(
    "numb_account, expected",
    [
        ("12345678876543211234", "**1234"),
        ("7158300734745758", "Некорректный ввод."),
        ("46894085699", "Некорректный ввод."),
        ("678594853758465784269", "Некорректный ввод."),
        ("6785948537584657842", "Некорректный ввод."),
        ("", "Некорректный ввод."),
        ("458345gfg893048", "Некорректный ввод."),
    ],
)
def test_mask_account_normal(numb_account, expected):
    assert get_mask_account(numb_account) == expected
