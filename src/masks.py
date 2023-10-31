
def get_hide(card: str):
    """
    Функция получает номер карты и прячет все символы,
    не включая последние четыре
    """
    return f'{card[:4]} {card[4:6]}** **** {card[-4:]}'


def get_bill(bill: str):
    """
    Функция получает номер счета, оставляя
    только последние четыре знака.
    Остальные скрыты за '**'
    """
    return f'**{bill[-4:]}'


print(get_hide('8990922113665229'))
print(get_bill('8990922113665229'))
