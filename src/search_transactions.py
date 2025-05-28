import re


def search_transactions(transactions: list, search_string: str) -> list:
    """
    Функция для поиска транзакций по заданной строке
    """
    # Компилируем регулярное выражение для поиска
    pattern = re.compile(search_string, re.I)  # Игнорируем регистр

    # Фильтруем транзакции по совпадению с регулярным выражением
    same_transactions = [
        transaction
        for transaction in transactions
        if "description" in transaction and pattern.search(transaction["description"])
    ]

    return same_transactions
