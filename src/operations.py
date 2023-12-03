import re


def get_operations(data: list[dict], search: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых есть строка с описанием
    :param data: list[dict] с данными
    :param search: str с описанием операции
    :return:
    """
    new_transaction = []
    for element in data:
        description = element["description"]
        try:
            if re.search(search, description):
                new_transaction.append(element)
        except KeyError:
            continue
        except TypeError:
            continue
    return new_transaction


def get_filter_dict(transactions: list[dict], category: dict) -> dict:
    """
    Функция принимает на вход список словарей с данными о банковских операциях и словарь категорий.
    Возвращает словарь с названиями категорий и количеством операций в каждой.
    :param transactions: list[dict] с данными
    :param category: dict с названием категорий
    :return:
    """
    for operation in transactions:
        try:
            for keys in category:
                if keys.upper() in operation["description"].upper():
                    category[keys] += 1
        except AttributeError:
            continue
    return category


# print(get_operations([
#   {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },
#   {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }], 'Перевод'))
