"""The tests for day22."""
from days import day22
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data([['..#', '#..', '...'], '5587'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day22.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day22.part_a(util.get_file_contents('day22.txt'))
        self.assertEqual(result, '5240')

    @data([['..#', '#..', '...'], '2511944'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day22.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day22.part_b(util.get_file_contents('day22.txt'))
        self.assertEqual(result, '2512144')
