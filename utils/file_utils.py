import json
from typing import List, Dict


def load_json_data(file_path: str) -> List[Dict[str, str]]:
    """
    JSONファイルからデータを読み込む関数

    Args:
        file_path (str): 読み込むJSONファイルのパス

    Returns:
        List[Dict[str, str]]: 読み込んだJSONデータのリスト
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def display_data(data: List[Dict[str, str]]) -> None:
    """
    JSONデータの各アイテムの情報を表示する関数

    Args:
        data (List[Dict[str, str]]): 表示するJSONデータのリスト
    """
    for item in data:
        japanese = item["japanese"]
        english = item["english"]
        key_phrase = item["key_phrase"]
        description = item["description"]

        print(f"Japanese: {japanese}")
        print(f"English: {english}")
        print(f"Key Phrase: {key_phrase}")
        print(f"Description: {description}")
        print("---")
