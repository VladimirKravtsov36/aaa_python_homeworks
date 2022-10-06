import pytest
from unittest.mock import patch
import what_is_year_now
import io


def test_dash_format():
    """
    Формат даты с тире
    """

    data = io.StringIO('{"currentDateTime": "2022-10-06"}')

    with patch('what_is_year_now.urllib.request.urlopen') as mocked_urlopen:
        mocked_urlopen.return_value = data
        assert what_is_year_now.what_is_year_now() == 2022
        mocked_urlopen.assert_called_once()


def test_dot_format():
    """
    Формат даты с точкой
    """

    data = io.StringIO('{"currentDateTime": "06.10.2022"}')

    with patch('what_is_year_now.urllib.request.urlopen') as mocked_urlopen:
        mocked_urlopen.return_value = data
        assert what_is_year_now.what_is_year_now() == 2022
        mocked_urlopen.assert_called_once()


def test_value_error():
    """
    Пример, когда дата не соответствует ни одному формату
    """

    data = io.StringIO('{"currentDateTime": "broken date"}')

    with patch('what_is_year_now.urllib.request.urlopen') as mocked_urlopen:
        mocked_urlopen.return_value = data

        with pytest.raises(ValueError):
            what_is_year_now.what_is_year_now()

        mocked_urlopen.assert_called_once()
