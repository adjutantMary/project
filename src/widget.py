from src.masks import get_hide, get_bill


def get_hided(bill_number: str):
    """
    Функция маскирует номер карты или счета.
    :param bill_number: Номер счета
    :return: С помощью срезов маскирует номер счета или карты
    """

    splitted_number = bill_number.split(" ")  # ['Visa', 'Platinum', '888']
    alpha_list = []
    digit_list = []
    for symbol in splitted_number:
        if symbol.isalpha():
            alpha_list.append(symbol)
        else:
            digit_list.append(symbol)

    if "Счет" in alpha_list:
        return f"Счет **{get_bill(digit_list[0])}"
    else:
        return f'{" ".join(alpha_list)} {get_hide(digit_list[0])}'


def get_data(data: str):
    """
    Функция принимает строку, возвращая измененную строку, форматируя ее в формат даты
    :param data: Строка для форматирования
    :return: Отформатированную строку формата дд.мм.гг
    """

    data_string = data[0:10].split("-")
    return f"{data_string[2]}.{data_string[1]}.{data_string[0]}"


# print(get_hided("Счет 73654108430135874305"))
# print(get_data("2018-07-11T02:26:18.671407"))
