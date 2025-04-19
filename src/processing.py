from typing import Dict, List


def filter_by_state(info_list: List[Dict],
                    state: str = 'EXECUTED') -> List[Dict]:
    """The function returns the list of dictionaries
    with 'EXECUTED' key state"""
    return [item for item in info_list if item.get("state") == state]


