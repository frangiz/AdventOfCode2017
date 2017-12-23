"""The tests for day23."""
from days import day23
from ddt import ddt
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    '''
    --- No examples for part a ---

    @data(
        [],
        []
        )
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day23.part_a(test_input)
        self.assertEqual(result, expected)'''

    def test_answer_part_a(self): # noqa D102
        result = day23.part_a(util.get_file_contents('day23.txt'))
        self.assertEqual(result, '6241')

    '''
    --- No examples for part b ---

    @data(
        [],
        []
        )
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day23.part_b(test_input)
        self.assertEqual(result, expected)'''

    def test_answer_part_b(self): # noqa D102
        result = day23.part_b(util.get_file_contents('day23.txt'))
        self.assertEqual(result, '909')
