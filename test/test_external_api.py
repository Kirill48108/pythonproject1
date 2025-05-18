
from unittest.mock import patch, MagicMock
from src.external_api import get_exch_rate
import json
@patch('requests.get')
def test_get_exch_rate(mock_get):

    mock_response = MagicMock()
    mock_response.text = json.dumps({'info': {'rate': 88.833612}})
    mock_get.return_value = mock_response
    assert get_exch_rate('USD', 'тут_мой_ключ_API') == 88.833612