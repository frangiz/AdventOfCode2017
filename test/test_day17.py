"""The tests for day17."""
from days import day17
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data([['3'], '638'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day17.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day17.part_a(util.get_file_contents('day17.txt'))
        self.assertEqual(result, '204')

    '''
    --- No examples for part b ---

    @data([])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day17.part_b(test_input)
        self.assertEqual(result, expected)'''

    def test_answer_part_b(self): # noqa D102
        result = day17.part_b(util.get_file_contents('day17.txt'))
        self.assertEqual(result, '28954211')
