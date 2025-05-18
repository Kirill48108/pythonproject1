import json
import random


def transaction():
    """Функция чтения JSON-файла возвращает список словарей с данными о финансовых транзакциях"""
    while True:
        with open("../data/operations.json", encoding="UTF-8") as file:
            content = json.load(file)
            content_random = random.choice(content)
            yield content_random
