from days import day02
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data(
        [['5 1 9 5', '7 5 3', '2 4 6 8'], '18']
        )
    @unpack
    def test_example_a(self, test_input, expected):
        result = day02.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day02.part_a(util.get_file_contents('day02.txt'))
        self.assertEqual(result, '53460')

    @data(
        [['5 9 2 8', '9 4 7 3', '3 8 6 5'], '9']
        )
    @unpack
    def test_example_b(self, test_input, expected):
        result = day02.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day02.part_b(util.get_file_contents('day02.txt'))
        self.assertEqual(result, '282')
