import unittest
from src.main import *


class RpnTesting(unittest.TestCase):
    def test_single_value(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("2")
        self.assertEqual(2, rpn_calculator.result)

    def test_decimal_input(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("1.2 - 1")
        self.assertEqual(rpn_calculator.result, None)

    def test_add(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("1 2 +")
        self.assertEqual(3, rpn_calculator.result)

    def test_subtract(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("1 2 -")
        self.assertEqual(-1, rpn_calculator.result)

    def test_divide(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("5 2 /")
        self.assertEqual(2, rpn_calculator.result)

    def test_multiply(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("5 6 *")
        self.assertEqual(30, rpn_calculator.result)

    def test_modulo(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("5 3 %")
        self.assertEqual(2, rpn_calculator.result)

    def test_multiple_valid_operators(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("5 5 + 4 - 2 /")
        self.assertEqual(3, rpn_calculator.result)

    def test_alpha_char(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("a 2 +")
        self.assertEqual(rpn_calculator.result, None)

    def test_too_many_operators(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("1 + + -")
        self.assertEqual(rpn_calculator.result, None)

    def test_too_few_operators(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("1 2 3 4 -")
        self.assertEqual(rpn_calculator.result, None)

    def test_no_space(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("53%")
        self.assertEqual(rpn_calculator.result, None)

    def test_double_space(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("5  3 -")
        self.assertEqual(rpn_calculator.result, 2)

    def test_division_by_zero(self):
        rpn_calculator = RPN()
        rpn_calculator.evaluate("5 0 /")
        self.assertEqual(rpn_calculator.result, None)


if __name__ == '__main__':
    unittest.main()
