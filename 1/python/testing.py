import unittest
from funcs import find_multiples


class test_find_multiples(unittest.TestCase):

    def test_find_multiples_3_or_5(self):
        self.assertEqual(set(find_multiples([3, 5], 10)), {3, 5, 6, 9})

    def test_find_multiples_2_or_5(self):
        self.assertEqual(set(find_multiples([2, 5], 10)), {2, 4, 5, 6, 8})

    def test_find_multiples_no_numbers(self):
        self.assertEqual(set(find_multiples([], 10)), set())


if __name__ == '__main__':
    unittest.main()