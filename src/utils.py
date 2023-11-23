import json
import logging
import os
from json import JSONDecodeError
from typing import Any


logger = logging.getLogger(__name__)
if os.path.exists("utils.log"):
    os.unlink("utils.log")
file_handler = logging.FileHandler("utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_json_file(path: str) -> list[dict[Any, Any]]:
    """
    Функция принимает на вход путь до JSON файла и
    возвращает список транцакций
    :param path: Путь к файлу типа str
    :return: list[dict]
    """
    file_logger = logging.getLogger(__name__)
    try:
        with open(path, encoding="UTF-8") as file:
            json_dict = json.load(file)
            file_logger.info("Выгрузка JSON - словаря")
            return json_dict
    except JSONDecodeError:
        file_logger.error("JSONDecodeError: JSON-файл имеет неправильный формат")
        return []
    except FileNotFoundError:
        file_logger.error("FileNotFoundError: Файл не найден")
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
    transaction_logger = logging.getLogger(__name__)
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        transaction_logger.info(f'Номер транзацкции: {float(transaction["operationAmount"]["amount"])}')
        return float(transaction["operationAmount"]["amount"])

    else:
        transaction_logger.error("ValueError: Транзация выполнена не в рублях. Укажите транзакцию в рублях")
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
