import unittest
from funcs import find_multiples_generator
from funcs import find_multiples_3_or_5

multiples_three = find_multiples_generator(3)

class test_find_multiples_generator(unittest.TestCase):
    def test_find_multiples_three(self):
        self.assertEqual(find_multiples_generator(3)(10), [3, 6, 9])


class test_find_multiples_3_or_5(unittest.TestCase):
    def test_find_multiples_3_or_5(self):
        self.assertEqual(find_multiples_3_or_5(10), [3, 5, 6, 9])





if __name__ == "__main__":
    unittest.main()


# from funcs import get_primes
# from funcs import factors_generator
# from funcs import factors_generator2



# class test_get_primes(unittest.TestCase):
#     def test_primes_till_10(self):
#         self.assertEqual(get_primes(10), [2, 3, 5, 7])

#     def test_primes_if_0(self):
#         self.assertEqual(get_primes(0), [])

#     def test_negative_n(self):
#         self.assertEqual(get_primes(-5), [])

#     def test_primes_if_1(self):
#         self.assertEqual(get_primes(1), [])

#     def test_primes_till_7(self):
#         self.assertEqual(get_primes(10), [2, 3, 5, 7])


# class test_factor_generator(unittest.TestCase):
#     def test_find_factors_of_100(self):
#         self.assertEqual(factors_generator(100)(100), [(2,2), (5, 2)])

#     def test_find_factors_of_0(self):
#         self.assertEqual(factors_generator(100)(0), [])

#     def test_find_factors_of_0(self):
#         self.assertEqual(factors_generator(20)(20), [(2, 2), (5, 1)])

# class test_factor_generator2(unittest.TestCase):
#     def test_find_factors_of_100(self):
#         self.assertEqual(factors_generator2(100)(100), [(2,2), (5, 2)])

#     def test_find_factors_of_0(self):
#         self.assertEqual(factors_generator2(100)(0), [])

#     def test_find_factors_of_0(self):
#         self.assertEqual(factors_generator2(20)(20), [(2, 2), (5, 1)])

