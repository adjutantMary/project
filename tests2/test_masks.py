import pytest
from src.masks import get_hide, get_bill


@pytest.fixture
def num():
    return "8990922113665229"


def test_masks_correct_work(num):
    assert get_bill(num) == "Некорректно введенные данные"
    assert get_hide(num) == "8990 92** **** 5229"
    assert type(get_bill(num)) == str
    assert type(get_hide(num)) == str
