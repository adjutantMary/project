import json
import os.path
import pytest
from data.path import PATH
from src.utils import get_json_file, get_transactions


@pytest.fixture
def path_to_transaction_rub():
    with open(os.path.join(PATH, "test_rub.json"), encoding="UTF-8") as file:
        json_file = json.load(file)

    return json_file


@pytest.fixture
def path_to_transaction_usd():
    with open(os.path.join(PATH, "test_usd.json"), encoding="UTF-8") as file:
        json_file = json.load(file)

    return json_file


@pytest.mark.parametrize(
    "path, expected_result",
    [
        (
            os.path.join(PATH, "test_rub.json"),
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
        ),
        (os.path.join(PATH, "test_unjson.json"), []),
        (os.path.join(PATH, "test_empty.json"), []),
        (os.path.join(PATH, "test.json"), []),
    ],
)
def test_get_json_file(path, expected_result):
    assert get_json_file(path) == expected_result


def test_get_transactions(path_to_transaction_rub):
    assert get_transactions(path_to_transaction_rub) == 31957.58


def test_transactions_error_predict(path_to_transaction_usd):
    with pytest.raises(ValueError):
        get_transactions(path_to_transaction_usd)
