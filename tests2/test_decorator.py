import os.path
from datetime import datetime

from src.decorators import log


def test_decorator_log():
    filename = 'test.txt'
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename)
    def foo(x: int, y: int) -> float:
        return x / y

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    foo(1, 2)

    with open(filename) as file:
        message = file.read().strip()

    expected_return = f'{time}.foo ok'



    assert message == expected_return






