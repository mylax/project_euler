import unittest
from funcs import primes, find_factors


class test_primes_(unittest.TestCase):

    def test_find_up_to_ten(self):
        self.assertEqual(list(primes(10)), [2, 3, 5, 7])

    def test_find_up_to_0(self):
        self.assertEqual(list(primes(0)), [])

    def test_find_up_to_7(self):
        self.assertEqual(list(primes(7)), [2, 3, 5, 7])


class test_find_factors(unittest.TestCase):

    def test_biggest_factor_10(self):
        self.assertEqual(find_factors(10), 5)

    def test_biggest_factor_1(self):
        self.assertEqual(find_factors(1), 1)

    def test_biggest_factor_7(self):
        self.assertEqual(find_factors(7), 7)


if __name__ == '__main__':
    unittest.main()