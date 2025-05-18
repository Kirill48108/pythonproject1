import json
import os
import requests



my_api = os.getenv("API_KEY")

def get_exch_rate(curr: str , my_api: str) -> float:
    """Функция возвращает курс валюты по отношению к рублю, обращаясь к АПИ apilayer.com"""
    headers: dict = {"apikey": my_api}
    url_frmtted = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=" + curr + "&amount=15000"

    response = requests.get(url_frmtted, headers=headers)
    result_pyth = json.loads(response.text)
    result = result_pyth["info"]["rate"]
    return result
