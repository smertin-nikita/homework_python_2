from datetime import datetime


def log(file_path=None):
    file_path = file_path or 'log.txt'

    def decorator(func):
        def inner(*args, **kwargs):
            result = func(*args)
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(
                    f'{func} '
                    f'params: {args} {kwargs} '
                    f'{datetime.today().strftime("%d-%m-%Y %H:%M:%S")} '
                    f'return: {result} \n')
            return result
        return inner
    return decorator

