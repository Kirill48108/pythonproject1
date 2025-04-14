from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_of_account: str) -> str:
    """Функция принимает номер карты/счёта с указанием ее типа"""
    card_of_account_list = card_of_account.split()
    if "Счёт" in card_of_account_list:
        return f"Счёт {get_mask_account(card_of_account_list[1])}"
    elif "MasterCard" in card_of_account_list or "Maestro" in card_of_account_list:
        return f"{card_of_account_list[0]} {get_mask_card_number(card_of_account_list[1])}"
    elif "Visa" in card_of_account_list:
        numbers_card = []
        name_card = []
        for i in card_of_account_list:
            if i.isdigit():
                numbers_card.append(i)
            elif i.isalpha():
                name_card.append(i)
        str_numbers_card = "".join(numbers_card)
        return f"{name_card[0]} {name_card[1]} {get_mask_card_number(str_numbers_card)}"


def get_date(my_date: str) -> str:
    """Функция конвертирования даты"""
    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
