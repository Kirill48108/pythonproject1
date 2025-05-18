from unittest.mock import patch, mock_open
import unittest


class TestTransactionFunction(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1}]')
    @patch('json.load', return_value=[{"id": 1}])
    def test_transaction(self, mock_json_load, mock_open):
        from src.utils import transaction
        result = next(transaction())
        self.assertEqual(result, {"id": 1})


if __name__ == '__main__':
    unittest.main()