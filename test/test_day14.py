from days import day14
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data([['flqrgnkx'], '8108'])
    @unpack
    def test_example_a(self, test_input, expected):
        result = day14.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day14.part_a(util.get_file_contents('day14.txt'))
        self.assertEqual(result, '8292')

    @data([['flqrgnkx'], '1242'])
    @unpack
    def test_example_b(self, test_input, expected):
        result = day14.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day14.part_b(util.get_file_contents('day14.txt'))
        self.assertEqual(result, '1069')
