from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция принимает на вход сообщение вида: '<Вид банковской карты/счет> <номер>' и
    выводит замаскированный счёт карты/банковского счёта
    в соответсвии с шаблоном: '<Вид банковской карты/счет> <*****>'
    """
    # Разбиваем вводные данные на вид банковской карты/счет и номер
    number_info = number.split()
    # Проверяем введён ли вид банковской карты/счет.
    # В случае отсутствия вида банковской карты/счета выводим сообщение об ошибке в введённых данных.
    if len(number_info) == 1:
        result_message = "Ошибка в введённых данных!"
    else:
        # Проверяем, какой номер был введён: карты либо банковского счёта.
        # Выбираем необходимую функцию из модуля "masks".
        # Применяем функции из модуля "masks".
        # Проверяем результат работы функции маскировки: сообщение об ошибке либо маска.
        # Формируем и выводим результирующее сообщение.
        if number_info[0] == "Счет" or number_info[0] == "Счёт":
            if "*" in get_mask_account(number_info[-1]):
                result_message = f"{number_info[0]} {get_mask_account(number_info[-1])}"
            else:
                result_message = get_mask_account(number_info[-1])
        else:
            if "*" in get_mask_card_number(number_info[-1]):
                result_message = f"{' '.join(number_info[:-1])} {get_mask_card_number(number_info[-1])}"
            else:
                result_message = get_mask_card_number(number_info[-1])
    return result_message


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
