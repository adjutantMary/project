from src.masks import get_hide, get_bill


def get_hided(bill_number: str):
    """
    Принимает на вход строку информацией тип карты/счета и номер карты/счета
    Возвращает эту строку с замаскированным номером карты/счета
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
    Принимает строку, возвращая измененную строку в формате даты
    """

    data_string = data[0:10].split("-")
    return f"{data_string[2]}.{data_string[1]}.{data_string[0]}"


print(get_hided("Visa Platinum 8990922113665229"))
print(get_data("2018-07-11T02:26:18.671407"))
