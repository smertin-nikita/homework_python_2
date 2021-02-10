import sys

import ijson
import json

FILE_PATH = 'countries.json'


class Founder:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, encoding='utf-8') as f:
            self.objects = ijson.items(f, 'item.name.common')
            print(sys.getsizeof(self.objects))
            countries_name = (o for o in self.objects)
            for item in countries_name:
                print(item)

            self.countries = json.load(f)
            print(sys.getsizeof(self.countries))

    def __iter__(self):
        return self

    def __next__(self):
        pass


if __name__ == '__main__':
    founder = Founder(FILE_PATH)
