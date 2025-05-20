import logging
import sys
from functools import wraps


def log(filename=None):
    """Декоратор log который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""
    if filename:
        logging.basicConfig(
            filename=filename, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", encoding="utf-8"
        )
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", stream=sys.stdout)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logging.info(f'Начало выполнения функции "{func.__name__}" c аргументами: {args} {kwargs}')
                result = func(*args, **kwargs)
                logging.info(f'Функция "{func.__name__}" завершилась успешно с результатом: {result}')
                return result
            except Exception as e:
                logging.error(f'Ошибка в функции "{func.__name__}": {type(e).__name__} с аргументами: {args} {kwargs}')
                raise

        return wrapper

    return decorator


@log()
def divide(x, y):
    return x / y


@log(filename="app.log")
def faulty_function(x):
    return x / 0  # Это вызовет ошибку


# Тестируем функции
print(divide(10, 2))
try:
    faulty_function(10)
except ZeroDivisionError:
    pass
