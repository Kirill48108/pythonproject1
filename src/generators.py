from typing import Any, Iterator


def card_number_generator(start=1, stop=100000000000000000) -> Iterator[str]:
    """Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    if stop > 9999999999999999:
        raise ValueError
    start_card_number = "0000000000000000"
    nums = (num for num in range(start, stop + 1))
    for num in nums:
        card_number = start_card_number[: -len(str(num))] + str(num)
        if len(card_number) > 16:
            raise ("В номере карты не может быть больше 16 цифр")
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Функция принимает на вход список со словарем и возвращает id операции"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Any:
    """который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX ,где X— цифра номера карты."""
    try:
        for description_operation in transactions:
            yield description_operation.get("description")
    except StopIteration:
        if transactions == []:
            return "None"
