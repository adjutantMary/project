def get_state(state: str, states_list: list) -> list:
    '''
    Функция получает на вход список словарей и возвращает словари, соответствующие ключу state.
    :param state: Опциональный пораметр(ключ)
    :param states_list: Список словарей, содержащие один из двух ключей
    :return: Список словарей, которые соответсвуют опциональному параметру
    '''

    new_list = []
    for word in states_list:
        if word["state"] == state:
            new_list.append(word)
    return new_list


def get_sorted(states_list: list, type_sort: str):
    '''
    Функция получает на вход список словарей и сортирует по дате.
    :param states_list: Список со словарем
    :param type_sort: Тип сортировки - по возрастанию 'High', или по убыванию 'Low'
    :return: Сортированный в зависимости от значения type_sort список
    '''
    if type_sort == "High":
        return sorted(states_list, key=lambda x: x["date"])
    else:
        return sorted(states_list, key=lambda x: x["date"], reverse=True)


# print(
#     get_state(
#         "EXECUTED",
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ],
#     )
# )
# print(
#     get_sorted(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ],
#         "High"
#     )
# )
