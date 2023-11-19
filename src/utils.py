import json
from json import JSONDecodeError
from typing import Any


def get_json_file(path: str) -> list[dict[Any, Any]]:
    """
    Функция принимает на вход путь до JSON файла и
    возвращает список транцакций
    :param path: Путь к файлу типа str
    :return: list[dict]
    """
    try:
        with open(path, encoding="UTF-8") as file:
            json_dict = json.load(file)
            return json_dict
    except JSONDecodeError:
        print("JSON-файл имеет неправильный формат ")
        return []
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except FileExistsError:
        print("Файл не существует")
        return []


def get_transactions(transaction: dict) -> float:
    """
    Функция получает транзакцию и возвращает результат типа float в зависимости от типа code
    :param transaction: Принимает транзакцию типа dict
    :return:
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])

    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
