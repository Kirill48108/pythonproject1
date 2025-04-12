from typing import Union

card_number: str = input("Введите номер карты :")
account_number: str = input("Введите номер счета :")
"""Получаем данные от пользователя"""


def get_mask_card_number(card_number: [str]) -> [str]:
    """Возвращаем замаскированный номер карты"""
    len_number = 16
    if len(card_number) == len_number and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return "Вы ввели некорректные данные ! "


def get_mask_account(account_number: [str]) -> [str]:
    """Возвращаем замаскированный номер счета"""
    len_acc_number = 20
    if len(account_number) == len_acc_number and account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        return "Вы ввели некорректные данные ! "
