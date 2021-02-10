import sys
import time

import ijson
import json

FILE_PATH = 'countries.json'



def founder(file_path):
    with open(file_path, encoding='utf-8') as f:
        objects = ijson.items(f, 'item.name.common')
        for item in objects:
            yield item, f"https://en.wikipedia.org/wiki/{item.replace(' ', '_')}"
        print(sys.getsizeof(objects))


class Founder:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, encoding='utf-8') as f:
            self.countries = iter(json.load(f))
        print(sys.getsizeof(self.countries))

    def __iter__(self):
        return self

    def __next__(self):
        country = next(self.countries)['name']['common']
        return country, f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"


if __name__ == '__main__':
    start_time = time.time()
    founder_class = Founder(FILE_PATH)
    # for item in founder_class:
    #     print(item)
    founder_class_time = time.time() - start_time

    start_time = time.time()
    founder_gen = founder(FILE_PATH)
    for item in founder_gen:
        print(item)
    founder_gen_time = time.time() - start_time

    print(f"class size = {sys.getsizeof(founder_class)}")
    print(f"gen size = {sys.getsizeof(founder_gen)}")
    print(f"class time = {founder_class_time}")
    print(f"gen time = {founder_gen_time}")
