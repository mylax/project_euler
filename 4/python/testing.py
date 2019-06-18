import unittest
from funcs import is_palindromic, find_palindromic


class test_is_palindromic(unittest.TestCase):

    def test_if_00_is_palindromic(self):
        self.assertTrue(is_palindromic(33))

    def test_if_002300_is_palindromic(self):
        self.assertTrue(is_palindromic(5655565))

    def test_if_99999_is_palindromic(self):
        self.assertTrue(is_palindromic(99999))



class test_find_palindromic(unittest.TestCase):

    def test_biggest_palindromic_to_ten(self):
        self.assertEqual(find_palindromic(10, 1)["prod"], 9)

    def test_biggest_palindromic_to_100(self):
        self.assertEqual(find_palindromic(100, 1)["prod"], 99)

    def test_biggest_factor_7(self):
        self.assertEqual(find_palindromic(10, 10)["prod"], 9)


if __name__ == '__main__':
    unittest.main()