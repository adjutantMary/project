
def get_state(state: str, states_list: list):

    '''
   Функция принимает на вход список states_list и опц.параметр state
   Возвращает новый список, содержащий только те словари,
   у которых ключ state содержит переданное в функцию значение
    '''

    new_list = []
    for word in states_list:
        if word['state'] == state:
            new_list.append(word)
    return new_list

print(get_state('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
