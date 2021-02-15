from datetime import datetime


def log(func):
    def inner(*args, **kwargs):
        result = func()
        with open('log.txt', 'w', encoding='utf-8') as f:
            f.write(f'function {func.func_name} {args} {kwargs} {datetime.today()} {result}')
        return result
    return inner
