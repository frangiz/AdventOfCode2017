"""The tests for day24."""
from days import day24
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data([['0/2',
            '2/2',
            '2/3',
            '3/4',
            '3/5',
            '0/1',
            '10/1',
            '9/10'], '31'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day24.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day24.part_a(util.get_file_contents('day24.txt'))
        self.assertEqual(result, '1511')

    @data([['0/2',
            '2/2',
            '2/3',
            '3/4',
            '3/5',
            '0/1',
            '10/1',
            '9/10'], '19'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day24.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day24.part_b(util.get_file_contents('day24.txt'))
        self.assertEqual(result, '1471')
