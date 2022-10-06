import pytest
from ohe import fit_transform


def test_many_args():
    """
    Несколько элементов,
    среди которых есть повторяющиеся
    """
    args = ['Moscow', 'New York', 'Moscow', 'London']

    actual = fit_transform(args)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]

    assert actual == expected


def test_unique_args():
    """
    Все элементы уникальны
    """
    args = [1, 2, 3]

    actual = fit_transform(args)
    expected = [
        (1, [0, 0, 1]),
        (2, [0, 1, 0]),
        (3, [1, 0, 0]),
    ]

    assert actual == expected


def test_same_args():
    """
    Единственный уникальный элемент
    повторяется несколько раз
    """

    args = [1, 1, 1]
    actual = fit_transform(args)

    expected = [
        (1, [1]),
        (1, [1]),
        (1, [1]),
    ]

    assert actual == expected


def test_empty():
    """
    Пустая последовательность
    """
    args = []

    actual = fit_transform(args)
    expected = []

    assert actual == expected


def test_one_arg():
    """
    Один элемент
    """
    args = 'avito'

    actual = fit_transform(args)
    expected = [
                ('avito', [1])
                ]

    assert actual == expected


def test_no_args():

    """
    Вызов без аргументов
    """
    with pytest.raises(TypeError):
        fit_transform()
