def factorize(x):
    """ Factorize positive integer and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """
    pass


import unittest


class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        values = ['string', 1.5]
        for val in values:
            with self.subTest(x=val):
                self.assertRaises(TypeError, factorize, val)

    def test_negative(self):
        values = [-1, -10, -100]
        for val in values:
            with self.subTest(x=val):
                self.assertRaises(ValueError, factorize, val)

    def test_zero_and_one_cases(self):
        values = [0, 1]
        for val in values:
            with self.subTest(x=val):
                self.assertEqual(factorize(val), (val, ))

    def test_simple_numbers(self):
        values = [3, 13, 29]
        for val in values:
            with self.subTest(x=val):
                self.assertEqual(factorize(val), (val,))

    def test_two_simple_multipliers(self):
        values = [6, 26, 121]
        results = [(2, 3), (2, 13), (11, 11)]
        for val, res in zip(values, results):
            with self.subTest(x=val):
                self.assertEqual(factorize(val), res)

    def test_many_multipliers(self):
        values = [1001, 9699690]
        results = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
        for val, res in zip(values, results):
            with self.subTest(x=val):
                self.assertEqual(factorize(val), res)


if __name__ == '__main__':
    unittest.main()
