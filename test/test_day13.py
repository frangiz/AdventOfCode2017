from days import day13
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data([['0: 3', '1: 2', '4: 4', '6: 4'], '24'])
    @unpack
    def test_example_a(self, test_input, expected):
        result = day13.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day13.part_a(util.get_file_contents('day13.txt'))
        self.assertEqual(result, '632')

    @data([['0: 3', '1: 2', '4: 4', '6: 4'], '10'])
    @unpack
    def test_example_b(self, test_input, expected):
        result = day13.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day13.part_b(util.get_file_contents('day13.txt'))
        self.assertEqual(result, '3849742')
