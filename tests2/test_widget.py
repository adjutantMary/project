import pytest
from src.widget import get_hided, get_data

@pytest.mark.parametrize('string, expected_result',
                         [
                             ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                             ('Счет 73654108430135874305', 'Счет ****4305'),
                         ])
def test_get_hided_correct_work(string, expected_result):
    assert get_hided(string) == expected_result
    assert type(get_hided(string)) == str


def test_get_data_correct_work():
    assert get_data('2018-07-11T02:26:18.671407') == '11.07.2018'
    assert get_data('2002-12-02Q02:2JSQ2.QPSOE3') == '02.12.2002'
    assert type(get_data('2018-07-11T02:26:18.671407')) == str





