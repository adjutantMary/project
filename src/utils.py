import json
from json import JSONDecodeError
from typing import Union


def get_json_file(path: str) -> Union:
    '''

    :param path:
    :return:
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

