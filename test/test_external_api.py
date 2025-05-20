from src.external_api import convert_transaction
from unittest.mock import patch, MagicMock
from src.external_api import get_exch_rate
import json
import unittest
from unittest.mock import patch



class TestConvertTransaction(unittest.TestCase):
    @patch('src.external_api.get_exch_rate')
    def test_convert_transaction_usd(self, mock_get_exch_rate):

        mock_get_exch_rate.return_value = 75.0

        transaction = {
            "operationAmount": {
                "amount": 100.0,
                "currency": {
                    "code": "USD"
                }
            }
        }


        result = convert_transaction(transaction)
        self.assertEqual(result, 7500.0)

    def test_convert_transaction_rub(self):
        transaction = {
            "operationAmount": {
                "amount": 100.0,
                "currency": {
                    "code": "RUB"
                }
            }
        }

        result = convert_transaction(transaction)
        self.assertEqual(result, 100.0)

if __name__ == '__main__':
    unittest.main()


@patch('requests.get')
def test_get_exch_rate(mock_get):

    mock_response = MagicMock()
    mock_response.text = json.dumps({'info': {'rate': 88.833612}})
    mock_get.return_value = mock_response
    assert get_exch_rate('USD', 'тут_мой_ключ_API') == 88.833612

