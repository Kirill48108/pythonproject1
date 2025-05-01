from generators.generators import card_number_generator,transaction_descriptions,filter_by_currency
import  pytest

@pytest.mark.parametrize("transactions, currency", [
    ([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ], "USD")
])

def test_filter_by_currency(transactions, currency):
    filtered_transactions = filter_by_currency(transactions, currency)
    assert next(filtered_transactions)["id"] == 939719570

@pytest.mark.parametrize('index, expected', [(0, 'Перевод организации'), (1, 'Перевод со счета на счет'),(2,"Перевод с карты на карту")])

def test_transaction_descriptions_3(index, expected):

    transactions = [

        {'description': 'Перевод организации'},

        {'description': 'Перевод со счета на счет'},

        {'description': 'Перевод с карты на карту'}

    ]

    descriptions = list(transaction_descriptions(transactions))

    assert descriptions[index] == expected



@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 1, "0000 0000 0000 0001"),
        (9999, 10000, "0000 0000 0000 9999"),
        (99999999, 100000000, "0000 0000 9999 9999"),
    ],
)
def test_card_number_generator(start, stop, expected):
    generator = card_number_generator(start, stop)
    assert next(generator) == expected
