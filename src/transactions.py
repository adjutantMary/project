import pandas as pd
import json
import os
from data.path import PATH


def get_csv_transactions(path: str) -> dict:
    """
    Функция принимает на вход путь к csv - файлу с транзакциями, возвращая словарь
    :param path: имя файла типа str
    :return:словарь типа dict
    """
    with open(path, encoding="utf-8") as file:
        data = pd.read_csv(file)

    return data.to_dict("split")


def get_xlsx_transactions(path: str) -> dict:
    """
    Функция принимает на вход путь к xlsx - файлу с транзакциями, возвращая словарь
    :param path: имя файла типа str
    :return:словарь типа dict
    """
    with open(path, encoding="utf-8") as file:
        data = pd.read_excel(file)

    return data.to_dict("split")
