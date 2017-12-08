from days import day08
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data(
        [['b inc 5 if a > 1',
            'a inc 1 if b < 5',
            'c dec -10 if a >= 1',
            'c inc -20 if c == 10'], '1'])
    @unpack
    def test_example_a(self, test_input, expected):
        result = day08.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day08.part_a(util.get_file_contents('day08.txt'))
        self.assertEqual(result, '4567')

    @data(
        [['b inc 5 if a > 1',
            'a inc 1 if b < 5',
            'c dec -10 if a >= 1',
            'c inc -20 if c == 10'], '10'])
    @unpack
    def test_example_b(self, test_input, expected):
        result = day08.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day08.part_b(util.get_file_contents('day08.txt'))
        self.assertEqual(result, '5636')
