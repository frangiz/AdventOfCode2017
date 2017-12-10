from days import day10
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data([['3, 4, 1, 5'], 12])
    @unpack
    def test_example_a(self, test_input, expected):
        result = day10.knot_hash(5, test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day10.part_a(util.get_file_contents('day10.txt'))
        self.assertEqual(result, '29240')

    @data(
        [],
        []
        )
    @unpack
    def test_example_b(self, test_input, expected):
        result = day10.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day10.part_b(util.get_file_contents('day10.txt'))
        self.assertEqual(result, '')
