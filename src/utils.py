import json
from json import JSONDecodeError


def get_json_file(path: str) -> list[dict]:
    '''
    Функция принимает на вход путь до JSON файла и
    возвращает список транцакций
    :param path: Путь к файлу типа str
    :return: list[dict]
    '''

    try:
        with open(path)as file:
            json_dict = json.load(file)
            return json_dict
    except JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    except FileExistsError:
        return []


def get_transactions(transaction: dict) -> float:
    '''
    Функция получает транзакцию и возвращает результат типа float в зависимости от типа code
    :param transaction: Принимает транзакцию типа dict
    :return:
    '''
    for item in transaction:
        if item['operationAmount']['currency']['code'] == 'RUB':
            return float(item['operationAmount']['amount'])

        else:
            raise ValueError('Транзация выполнена не в рублях. Укажите транзакцию в рублях')







