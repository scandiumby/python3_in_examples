from unittest import TestCase

from char_counter_for_string.main import *


class CharCounterTest(TestCase):
    string_standart = 'cazbaazzadzdcczz' # a - 4, b - 1, c - 3, d - 2, z - 6

    def test_get_count_each_chars_in_string(self):
        dict_standart = {
            'a': 4,
            'b': 1,
            'c': 3,
            'd': 2,
            'z': 6,
        }
        self.assertDictEqual(dict_standart, get_count_each_chars_in_string(self.string_standart))

    def test_get_count_unique_chars_in_string(self):
        self.assertEqual(5, get_count_unique_chars_in_string(self.string_standart))