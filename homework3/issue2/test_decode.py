from utils import decode
import pytest


@pytest.mark.parametrize(
    'source_string, result',
    [
        ('', ''),
        ('... --- ...', 'SOS'),
        ('.-   ...- ..        -  ---', 'AVITO'),
        ('.- .- .- ..--- ----- ..--- ...--', 'AAA2023')
    ],
)
def test_decode(source_string: str, result: str):
    assert decode(source_string) == result
