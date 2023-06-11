import unittest
from array import array

from business.sanitizer import Sanitizer


class TestSanitizer(unittest.TestCase):

    def setUp(self) -> None:
        self.sanitizer = Sanitizer()

    def test_sanitize_request_monomial(self):
        # Arrange
        request_str = '2x'
        expected_result = array('f', [0.0, 2.0])

        # Act
        result = self.sanitizer.get_sanitized_equation_array(request_str)

        # Assert
        self.assertEqual(expected_result, result)

    def test_sanitize_request_two_term_polynomial(self):
        # Arrange
        request_str = '2x^2+5'
        expected_result = array('f', [5.0, 0.0, 2.0])

        # Act
        result = self.sanitizer.get_sanitized_equation_array(request_str)

        # Assert
        self.assertEqual(expected_result, result)

    def test_sanitize_request_cubic_term_polynomial(self):
        # Arrange
        request_str = '3x^5 +5x^2 + 2'
        expected_result = array('f', [2.0, 0.0, 5.0, 0.0, 0.0, 3.0])

        # Act
        result = self.sanitizer.get_sanitized_equation_array(request_str)

        # Assert
        self.assertEqual(expected_result, result)
