"""The tests for day25."""
from days import day25
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data([['Begin in state A.',
            'Perform a diagnostic checksum after 6 steps.',
            '',
            'In state A:',
            '  If the current value is 0:',
            '    - Write the value 1.',
            '    - Move one slot to the right.',
            '    - Continue with state B.',
            '  If the current value is 1:',
            '    - Write the value 0.',
            '    - Move one slot to the left.',
            '    - Continue with state B.',
            '',
            'In state B:',
            '  If the current value is 0:',
            '    - Write the value 1.',
            '    - Move one slot to the left.',
            '    - Continue with state A.',
            '  If the current value is 1:',
            '    - Write the value 1.',
            '    - Move one slot to the right.',
            '    - Continue with state A.'], '3'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day25.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day25.part_a(util.get_file_contents('day25.txt'))
        self.assertEqual(result, '5744')

    '''
    --- No examples for part b ---

    @data(
        [],
        []
        )
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day25.part_b(test_input)
        self.assertEqual(result, expected)'''

    '''
    --- No part b ---

    def test_answer_part_b(self): # noqa D102
        result = day25.part_b(util.get_file_contents('day25.txt'))
        self.assertEqual(result, '')'''
