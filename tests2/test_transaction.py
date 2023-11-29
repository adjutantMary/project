import pandas as pd
import pytest
import os
from data.path import PATH
from src.transactions import get_csv_transactions


# @pytest.fixture
# def path_to_csv():
#     with open(os.path.join(PATH, "test_csv.csv"), encoding="UTF-8") as file:
#         data = pd.read_csv(file)
#     return data.to_dict("split")


@pytest.mark.parametrize(
    "path",
    "expected_result",
    [
        (
            os.path.join(PATH, "test_csv.csv"),
            {
                'index': [0], 'columns': ['id;state;date;amount;currency_name;currency_code;from;to;description'],
                'data': [['650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации']]
            }

        )
    ]
)
def test_csv_transactions(path, expected_result):
    assert get_csv_transactions(path) == expected_result
