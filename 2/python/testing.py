import unittest
from funcs import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_limit_10(self):
        self.assertEqual(list(fibonacci(10)), [0, 1, 1, 2, 3, 5, 8])

    def test_limit_8(self):
        self.assertEqual(list(fibonacci(8)), [0, 1, 1, 2, 3, 5, 8])

    def test_limit_0(self):
        self.assertEqual(list(fibonacci(0)), [0])

    def test_limit_7(self):
        self.assertEqual(list(fibonacci(7)), [0, 1, 1, 2, 3, 5, ])





if __name__ == "__main__":
    unittest.main()