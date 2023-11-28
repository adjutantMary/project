import pandas as pd
import json


def get_csv_transactions(filename: str) -> dict:
    """
    Функция принимает на вход путь к csv - файлу с транзакциями, возвращая словарь
    :param filename: имя файла типа str
    :return:словарь типа dict
    """
    with open(filename, encoding="utf-8") as file:
        data = pd.read_csv(file)

    return data.to_dict("split")


def get_xlsx_transactions(filename: str) -> dict:
    """
    Функция принимает на вход путь к xlsx - файлу с транзакциями, возвращая словарь
    :param filename: имя файла типа str
    :return:словарь типа dict
    """
    with open(filename, encoding="utf-8") as file:
        data = pd.read_excel(file)

    return data.to_dict("split")
