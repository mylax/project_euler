import unittest
from funcs import find_all_factors, find_prime_factors


class test_primes_(unittest.TestCase):

    def test_find_up_to_ten(self):
        self.assertEqual(find_all_factors(10), [2, 5])

    def test_find_up_to_0(self):
        self.assertEqual(find_all_factors(0), [])

    def test_find_up_to_100(self):
        self.assertEqual(find_all_factors(100), [2, 2, 5, 5])


class test_find_factors(unittest.TestCase):

    def test_biggest_factor_10(self):
        self.assertEqual(find_prime_factors(10), {2:1, 5:1})

    def test_biggest_factor_1(self):
        self.assertEqual(find_prime_factors([10, 11]), {2:1, 5:1, 11:1})

    def test_biggest_factor_7(self):
        self.assertEqual(find_prime_factors([10, 11, 5]), {2:1, 5:1, 11:1})


if __name__ == '__main__':
    unittest.main()