import json
import unittest
from unittest.mock import patch

from src.external_api import convert_transaction


class TestConvertTransaction(unittest.TestCase):
    @patch("src.external_api.get_exch_rate")
    def test_convert_transaction_rub(self, mock_get_exch_rate):
        transaction = {"operationAmount": {"amount": 1000, "currency": {"code": "RUB"}}}
        result = convert_transaction(transaction)
        self.assertEqual(result, 1000)


class TestApiCall(unittest.TestCase):
    @patch("requests.get")
    def test_api_call(self, mock_get):

        mock_get.return_value.text = json.dumps({"rates": {"USD": 75.0}})
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"rates": {"USD": 75.0}}
        mock_get.return_value.text = json.dumps({"result": 75.0})

        response = convert_transaction({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}})
        self.assertEqual(response, 75.0)


if __name__ == "__main__":
    unittest.main()
