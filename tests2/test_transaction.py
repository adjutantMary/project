import pytest
import os

from src.transactions import get_csv_transactions


@pytest.fixture
def path():
    return 'C:\\Users\\lacrimosa\\Desktop\\home_task1b\\src\\transactions.csv'


def test_csv(path):
    assert type(get_csv_transactions(path)) == dict

