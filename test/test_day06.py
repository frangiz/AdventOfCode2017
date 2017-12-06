from days import day06
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data([['0 2 7 0'], '5'])
    @unpack
    def test_example_a(self, test_input, expected):
        result = day06.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day06.part_a(util.get_file_contents('day06.txt'))
        self.assertEqual(result, '11137')

    @data([['0 2 7 0'], '4'])
    @unpack
    def test_example_b(self, test_input, expected):
        result = day06.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day06.part_b(util.get_file_contents('day06.txt'))
        self.assertEqual(result, '1037')
