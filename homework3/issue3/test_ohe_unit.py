from ohe import fit_transform
import unittest


class TestOhe(unittest.TestCase):

    def test_many_args(self):
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

        self.assertEqual(actual, expected)

    def test_unique_args(self):
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

        self.assertEqual(actual, expected)

    def test_same_args(self):
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

        self.assertIn(1, expected[0])
        self.assertEqual(actual, expected)

    def test_empty(self):
        """
        Пустая последовательность
        """
        args = []

        actual = fit_transform(args)
        expected = []

        self.assertEqual(actual, expected)

    def test_one_arg(self):
        """
        Один элемент
        """
        args = 'avito'

        actual = fit_transform(args)
        expected = [
                    ('avito', [1])
                    ]

        self.assertEqual(actual, expected)

    def test_no_args(self):
        """
        Вызов без аргументов
        """

        with self.assertRaises(TypeError) as context:
            fit_transform()

        self.assertIsInstance(context.exception, TypeError)
        self.assertEqual('expected at least 1 arguments, got 0',
                         str(context.exception))
