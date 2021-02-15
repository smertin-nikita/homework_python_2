import hashlib
import sys
import time

import ijson
import json

from logger import log

FILE_PATH = 'countries.json'


def founder(file_path):
    """
    Гениратор, который по каждой стране из файла countries.json ищет страницу из википедии
    :param file_path:
    """
    with open(file_path, encoding='utf-8') as f:
        objects = ijson.items(f, 'item.name.common')
        for item in objects:
            yield {item: f"https://en.wikipedia.org/wiki/{item.replace(' ', '_')}"}


class Founder:
    """
    Класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии
    """
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, encoding='utf-8') as f:
            self.countries = iter(json.load(f))

    def __iter__(self):
        return self

    def __next__(self):
        country = next(self.countries)['name']['common']
        return {country: f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"}


def get_hash(file_path):
    """
    Генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
    :param file_path:
    """
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


@log('log.txt')
def write_to_file(iterable, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in iterable:
            f.write(f'{item}\n')


if __name__ == '__main__':
    start_time = time.time()
    write_to_file(Founder(FILE_PATH), 'countries_info.txt')
    founder_class_time = time.time() - start_time

    start_time = time.time()
    write_to_file(founder(FILE_PATH), 'countries_info_2.txt')
    founder_time = time.time() - start_time

    # Замерил скорость выполнения
    print(f"class time = {founder_class_time}")
    print(f"gen time = {founder_time}")

    # Вывести hash md5 строк
    # for hash in get_hash('countries_info.txt'):
        # print(hash)
