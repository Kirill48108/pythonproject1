import json
import os

import requests

my_api = os.getenv("API_KEY")


def get_exch_rate(curr: str, amount: float) -> float:
    """Функция возвращает курс валюты по отношению к рублю, обращаясь к АПИ apilayer.com"""
    headers: dict = {"apikey": my_api}
    url_frmtted = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=" + curr + f"&amount={amount}"

    response = requests.get(url_frmtted, headers=headers)
    result_pyth = json.loads(response.text)
    result = result_pyth["result"]
    return result


def convert_transaction(transaction: dict) -> float:
    """Функция конвертации"""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    else:
        return get_exch_rate(currency, amount)
