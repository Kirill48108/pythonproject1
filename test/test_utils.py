import json
from typing import Any
from unittest import mock


from src.utils import get_info_about_transactions






@mock.patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_open: Any) -> None:
    result = get_info_about_transactions("fake_path.json")
    assert result == []


@mock.patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_json_decode_error(mock_json_load: Any) -> None:
    result = get_info_about_transactions("fake_path.json")
    assert result == []

@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="invalid json")
@mock.patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_json_decode_error(mock_json_load, mock_open):
    result = get_info_about_transactions("fake_path.json")
    assert result == []