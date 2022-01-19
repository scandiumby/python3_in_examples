from unittest import TestCase

from char_counter_for_string.main import *


# Python3.8 tested
class CharCounterTest(TestCase):
    string_standart = 'аааБББрСя'
    russian_alphabet = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'

    def test_get_count_each_chars_in_string(self):
        dict_standart = {'С': 1, 'Б': 3, 'р': 1, 'я': 1, 'а': 3}
        self.assertDictEqual(dict_standart, get_count_each_chars_in_string(self.string_standart))

    def test_get_count_unique_chars_in_string(self):
        self.assertEqual(5, get_count_unique_chars_in_string(self.string_standart))

    def test_get_russian_chars_not_included_in_string(self):
        not_included_russian_chars = set('АбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯ')
        self.assertSetEqual(not_included_russian_chars, get_russian_chars_not_included_in_string(self.string_standart))