import functools
import time
from datetime import datetime


def print_runtime(func):
    """ Выводит время выполнения функции. """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__} - {time.time() - start_time} seconds')
        return result
    return inner


def log(file_path=None):
    file_path = file_path or 'log.txt'

    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args)
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(
                    f'{func.__name__} '
                    f'PARAMS - {args} {kwargs} '
                    f'CALL DATETIME - {datetime.today().strftime("%d/%m/%Y %H:%M:%S")} '
                    f'RETURN - {result} \n')
            return result
        return inner
    return decorator

