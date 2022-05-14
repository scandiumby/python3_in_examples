import unittest

from .main import parse_sequence


class PatternMatchingTest(unittest.TestCase):

    def test_parse_sequence_correct_sequence(self):
        test_data = ['value_1', 'value_2']
        result = parse_sequence(test_data)
        self.assertIsInstance(result, tuple)
        self.assertSequenceEqual(test_data, result)

    def test_parse_sequence_with_incorrect_sequence(self):
        test_data = 10
        with self.assertRaises(Exception):
            parse_sequence(test_data)