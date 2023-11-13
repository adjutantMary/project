from datetime import datetime
from functools import wraps
from typing import Any


def log(filename: str = None):
    def wrapper(function):
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                final_result = function(*args, **kwargs)
                message = f"{time} {function.__name__} ok\n"
            except Exception as error:
                message = f"{time} {function.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}\n"
                final_result = None
            if filename:
                with open(filename, "a") as file:
                    file.write(message)
            else:
                print(message)

            return final_result

        return inner

    return wrapper


# @log(filename="mylog.txt")
# def my_function(x, y):
#     return x + y
#
# my_function(1, 2)
