import unittest
from src.main import RPN


class RpnTesting(unittest.TestCase):
    def test_add(self):
        abc = RPN("1 2 +")
        abc.evaluate()
        self.assertEqual(3, abc.result)

    def test_subtract(self):
        abc = RPN("1 2 -")
        abc.evaluate()
        self.assertEqual(-1, abc.result)

    def test_divide(self):
        abc = RPN("5 2 /")
        abc.evaluate()
        self.assertEqual(2, abc.result)

    def test_multiply(self):
        abc = RPN("5 6 *")
        abc.evaluate()
        self.assertEqual(30, abc.result)

    def test_modulo(self):
        abc = RPN("5 3 %")
        abc.evaluate()
        self.assertEqual(2, abc.result)

    def test_alpha_char(self):
        abc = RPN("a 2 +")
        abc.evaluate()
        self.assertRaises(ValueError)

    def test_too_few_operators(self):
        abc = RPN("1 + + -")
        abc.evaluate()
        self.assertRaises(IndexError)

    def test_too_many_operators(self):
        abc = RPN("1 2 3 4 -")
        abc.evaluate()
        self.assertRaises(ValueError)


if __name__ == '__main__':
    unittest.main()
