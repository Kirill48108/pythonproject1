import json
import logging
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_info_about_transactions(path_to_file: str) -> Any:
    """Функция принимает путь к файлу с транзакциями и возвращает их"""
    try:
        logger.info(f"Получение данных из файла {path_to_file}")
        with open(path_to_file, encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError as expect_info:
        logger.error(f'Ошибка: файл "{path_to_file}" не найден')
        print(f"Файл не найден: {expect_info}")
        return []
    except json.JSONDecodeError as expect_info:
        logger.error(f"Ошибка при чтении json-файла из файла {path_to_file}")
        print(f"Ошибка декодирования файла: {expect_info}")
        return []


print(get_info_about_transactions("data/operations.json"))
print(get_info_about_transactions("[]"))
print(get_info_about_transactions("fghhdhdh"))
