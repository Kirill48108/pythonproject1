from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_of_account: str) -> str:
    """Функция принимает номер карты/счёта с указанием ее типа"""
    card_of_account_list = card_of_account.split()
    if "Счёт" in card_of_account_list:
        return f"Счёт {get_mask_account(card_of_account_list[1])}"
    elif "MasterCard" in card_of_account_list or "Maestro" in card_of_account_list:
        return f"{card_of_account_list[0]} {get_mask_card_number(card_of_account_list[1])}"
    elif "Visa" in card_of_account_list:
        return f"{card_of_account_list[0]} {get_mask_card_number(card_of_account_list[1])}"
    else:
        return "Некорректный ввод."
        numbers_card = []
        name_card = []
        for i in card_of_account_list:
            if i.isdigit():
                numbers_card.append(i)
            elif i.isalpha():
                name_card.append(i)
        str_numbers_card = "".join(numbers_card)
        return f"{name_card[0]} {name_card[1]} {get_mask_card_number(str_numbers_card)}"


def get_date(date: str) -> str:
    """Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку
    с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    if len(date) != 26 or len(date) == "":
        raise ValueError("Вы ввели неверный формат входных данных")
    elif int(day) > 31 or day == "00":
        raise ValueError("День указан неверно")
    elif int(month) > 12 or month == "00":
        raise ValueError("Месяц указан неверно")
    elif int(year) > 9000 or year == "0000":
        raise ValueError("Год указан неверно")
    else:
        return f"{day}.{month}.{year}"
