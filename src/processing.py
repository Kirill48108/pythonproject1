from typing import Dict, List


def filter_by_state(info_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция принимает список словарей и значение для ключа state(по умолчанию 'EXECUTED').
    возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    return [item for item in info_list if item.get("state") == state]


def sort_by_date(info_list: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки"""
    return sorted(info_list, key=lambda x: x["date"], reverse=True)
