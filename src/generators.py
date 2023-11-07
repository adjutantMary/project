from typing import Generator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def usd_generators(transactions: list, ping: str) -> Generator:
    '''
    Функция, которая принимает список словарей transactions, в зависимости от ping, возвращает генератор id
    :param transactions: Список словарей
    :param ping: Строку с указанием code
    :return: Generator
    '''
    for item in transactions:
        if item['operationAmount']['currency']['code'] == ping:
            yield item
        else:
            return print('Ошибка в указании параметра')


def description_translator(transactions: list) -> Generator:
    '''
    Функция принимает список словарей transactions и возвращает (генератор) по ключу description
    :param transactions: Список словарей
    :return: Generator
    '''
    for item in transactions:
        if item['description']:
            yield item['description']


def get_cards_number(start: int, end: int) -> Generator:
    '''
    Функция получает диапазон, в котором будет происходить генерирование форматированных строк с номерами карт
    :param start: Начало диапазона
    :param end: Конец диапазона
    :return: Отформатированные строки в указанном диапазоне
    '''
    for item in range(start, end + 1):
        card_number = f"{'0' * (16 - len(str(item)))}{item}"
        yield card_number[0:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[12:16]


# usd_transactions = usd_generators(transactions, "USD")
#
# for _ in range(2):
#     print(next(usd_transactions)["id"])

# descriptions = description_translator(transactions)
#
# for _ in range(5):
#     print(next(descriptions))


# for card_number in get_cards_number(1, 5):
#     print(card_number)
