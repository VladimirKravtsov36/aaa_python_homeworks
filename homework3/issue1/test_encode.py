from utils import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе

    >>> encode('SOS') # doctest: +NORMALIZE_WHITESPACE
    '...  ---    ...'

    >>> encode('SFPSKMLDWIPMDSKMO')
    '... ... ---'

    >>> encode(1)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable

    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
