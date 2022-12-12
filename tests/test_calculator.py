import unittest
import ..src.calculator as calculator

class TestSumma(unittest.TestCase):
    #test sum_numbers
    def test_sum_numbers_returns_sum_of_integers(self):
        result = calculator.sum_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_sum_numbers_works_with_negative_numbers(self):
        result = calculator.sum_numbers(-2, -3)
        self.assertEqual(result, -5)

    def test_sum_numbers_returns_sum_of_floats(self):
        result = calculator.sum_numbers(2.4, 3.2)
        self.assertEqual(result, 5.6)

    def test_sum_numbers_returns_sum_of_integer_and_float(self):
        result = calculator.sum_numbers(2, 3.2)
        self.assertEqual(result, 5.2)

    def test_sum_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.sum_numbers(1, "a")


    #test minus_numbers
    def test_minus_numbers_returns_minus_of_integers(self):
        result = calculator.minus_numbers(2, 3)
        self.assertEqual(result, -1)

    def test_minus_numbers_works_with_negative_numbers(self):
        result = calculator.minus_numbers(-2, -3)
        self.assertEqual(result, 1)

    def test_minus_numbers_returns_minus_of_floats(self):
        result = calculator.minus_numbers(2.4, 3.2)
        self.assertTrue((result - -0.8) < 0.0000000001)

    def test_minus_numbers_returns_minus_of_integer_and_float(self):
        result = calculator.minus_numbers(2, 3.2)
        self.assertTrue((result - -1.2) < 0.0000000001)

    def test_minus_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.minus_numbers(1, "a")
    

    #test divide_numbers
    def test_divide_numbers_returns_divide_of_integers(self):
        result = calculator.divide_numbers(3, 2)
        self.assertEqual(result, 1.5)

    def test_divide_numbers_works_with_negative_numbers(self):
        result = calculator.divide_numbers(-3, -2)
        self.assertEqual(result, 1.5)

    def test_divide_numbers_returns_divide_of_floats(self):
        result = calculator.divide_numbers(3.6, 0.6)
        self.assertEqual(result, 6)

    def test_divide_numbers_returns_divide_of_integer_and_float(self):
        result = calculator.divide_numbers(3, 0.2)
        self.assertEqual(result, 15)

    def test_divide_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.divide_numbers(1, "a")
