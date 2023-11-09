import pytest
from src.generators import usd_generators, description_translator, get_cards_number

@pytest.fixture
def list_group():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
@pytest.fixture
def type_code():
    return 'USD'


def test_usd(list_group, type_code):
    check_usd = list(usd_generators(list_group, type_code))
    for line in check_usd:
        if line['id']:
            assert line['id'] == 939719570


def test_translator(list_group):
    check_translation = list(description_translator(list_group))
    # for line in check_translation:
    #     if line['description']:
    assert check_translation == ['Перевод организации']


def test_cards_number():
    check_translation = list(get_cards_number(1, 5))
    assert check_translation == ['0000 0000 0000 0001',
                                 '0000 0000 0000 0002',
                                 '0000 0000 0000 0003',
                                 '0000 0000 0000 0004',
                                 '0000 0000 0000 0005'
                                 ]







