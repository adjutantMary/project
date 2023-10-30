
def get_hided(bill_number: str):
    '''
    Принимает на вход строку информацией тип карты/счета и номер карты/счета
    Возвращает эту строку с замаскированным номером карты/счета
    '''
    splitted_number = bill_number.split(' ')
    number = str(splitted_number[1])

    if 'Счет' in splitted_number:
        return f'Счет **{number[-4:]}'
    else:
        return f'{splitted_number[0]} {number[:4]} {number[4:6]}** **** {number[-4:]}'


def get_data(data: str):
    '''
    Принимает строку, возвращая измененную строку в формате даты
    '''

    data_string = data[0:9].split('-')
    return f'{data_string[1]}.{data_string[2]}.{data_string[0]}'

print(get_hided('Maestro 1596837868705199'))
print(get_data("2018-07-11T02:26:18.671407"))

