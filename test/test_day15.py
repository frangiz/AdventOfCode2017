from days import day15
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data(
        [['Generator A starts with 65', 'Generator B starts with 8921'], '588'])
    @unpack
    def test_example_a(self, test_input, expected):
        result = day15.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day15.part_a(util.get_file_contents('day15.txt'))
        self.assertEqual(result, '567')

    @data(
        [['Generator A starts with 65', 'Generator B starts with 8921'], '309'])
    @unpack
    def test_example_b(self, test_input, expected):
        result = day15.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day15.part_b(util.get_file_contents('day15.txt'))
        self.assertEqual(result, '323')
