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








