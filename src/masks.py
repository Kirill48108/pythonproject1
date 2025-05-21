import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Возвращаем замаскированный номер карты"""
    logger.info(f"Получение номера карты: {card_number}")
    len_card_number = 16
    logger.info("Проверка из 16 цифр состоит номер карты или нет")
    if len(card_number) == len_card_number and card_number.isdigit():
        logger.info("Результат работы функции get_mask_card_number получен")
        return f"{card_number [:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        logger.error("Некорректный ввод")
        return "Некорректный ввод."


print(get_mask_card_number("132214415522515"))
print(get_mask_card_number("1234567887654321"))
print(get_mask_card_number(" "))
print(get_mask_card_number("dsfhhhshfsh"))


def get_mask_account(account_number: str) -> str:
    """Возвращаем замаскированный номер счета"""
    logger.info(f"Получение номера счета: {get_mask_account}")
    len_acc_number = 20
    logger.info("Проверка из 20 цифр состоит номер счета или нет")
    if len(account_number) == len_acc_number and account_number.isdigit():
        logger.info("Результат работы функции get_mask_account получен")
        return f"**{account_number[-4:]}"
    else:
        logger.error("Некорректный ввод")
        return "Некорректный ввод."


print(get_mask_account("132214415522515"))
print(get_mask_account("12345678876543214567"))
print(get_mask_account(" "))
print(get_mask_account("dsfhhhshfsh"))
