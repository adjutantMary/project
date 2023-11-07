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
    assert usd_generators(list_group, type_code) == True



