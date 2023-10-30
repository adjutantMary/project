
def get_hided(name: str, number: int):
    '''
    Принимает на вход строку информацией тип карты/счета и номер карты/счета
    Возвращает эту строку с замаскированным номером карты/счета
    '''

    if name == 'Счет':
        return f'{name} **{number[-4:]}'
    else:
        return f'{name} {number[:4]} {number[4:6]}** **** {number[-4:]}'


def get_data(data: str):
    '''
    Принимает строку, возвращая измененную строку в формате даты
    '''

    data_string = data[0:9].split('-')
    return f'{data_string[1]}.{data_string[2]}.{data_string[0]}'

print(get_hided())
print(get_data())

