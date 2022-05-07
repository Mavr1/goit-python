from re import T
import re

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

mapper = {}

for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    mapper[ord(c)] = t
    mapper[ord(c.upper())] = t.capitalize()


def normalize(string: str) -> str:
    name = string.translate(mapper)
    return re.sub(r'\W', '_', name.strip())
