import json
from keyword import iskeyword
from typing import Dict


class JsonHandler:

    def __init__(self, mapping: Dict[str, str]):

        self._mapping = dict()

        for key, value in mapping.items():
            if iskeyword(key):
                self._mapping[f'{key}_'] = value
            else:
                self._mapping[key] = value

    def __getattr__(self, item: str) -> str:

        if isinstance(self._mapping[item], dict):
            return JsonHandler(self._mapping[item])

        return self._mapping[item]

    def __repr__(self) -> str:
        return f'{self._mapping}'


class ColorizeMixin:

    def __str__(self) -> str:
        return (f'\033[1;{self.repr_color_code};40m'
                f'{self.title} | {self.price} ₽')


class Advert(ColorizeMixin):

    repr_color_code = 32

    def __init__(self, mapping: Dict[str, str]):

        if 'price' not in mapping.keys():
            mapping['price'] = 0

        if mapping['price'] < 0:
            raise ValueError('must be >= 0')

        self._mapping = JsonHandler(mapping)

    def __getattr__(self, item: str) -> str:
        return self._mapping.__getattr__(item)

    def __repr__(self) -> str:
        return str(f'{self.title} | {self.price} ₽')


if __name__ == '__main__':

    lesson_str = """{
                    "title": "python", "class": "aaa",
                    "location": {
                    "address": {"city": "Москва", "building": "Лесная, 7"},
                    "metro_stations": ["Белорусская"]}
                    }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    print(lesson_ad)
    print(lesson_ad.title)
    print(lesson_ad.class_)
    print(lesson_ad.location)
    print(lesson_ad.location.address.city)

    corgy_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория \
Тишково, 25"
        }
        }"""

    corgy = json.loads(corgy_str)
    corgy_ad = Advert(corgy)

    print(corgy_ad)
    print(corgy_ad.price)
    print(corgy_ad.class_)
    print(corgy_ad.location)
