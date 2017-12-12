from days import day12
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data([['0 <-> 2',
            '1 <-> 1',
            '2 <-> 0, 3, 4',
            '3 <-> 2, 4',
            '4 <-> 2, 3, 6',
            '5 <-> 6',
            '6 <-> 4, 5'], '6'])
    @unpack
    def test_example_a(self, test_input, expected):
        result = day12.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day12.part_a(util.get_file_contents('day12.txt'))
        self.assertEqual(result, '175')

    @data([['0 <-> 2',
            '1 <-> 1',
            '2 <-> 0, 3, 4',
            '3 <-> 2, 4',
            '4 <-> 2, 3, 6',
            '5 <-> 6',
            '6 <-> 4, 5'], '2'])
    @unpack
    def test_example_b(self, test_input, expected):
        result = day12.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day12.part_b(util.get_file_contents('day12.txt'))
        self.assertEqual(result, '213')
