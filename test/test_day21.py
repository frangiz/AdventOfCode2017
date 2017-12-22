"""The tests for day21."""
from days import day21
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data([['../.# => ##./#../...',
            '.#./..#/### => #..#/..../..../#..#'], '12'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        rules = day21.parse_rules(test_input)
        start_grid = ('.#.', '..#', '###')
        new_grid = day21.expand(rules, start_grid, 2)
        result = str(day21.count(new_grid, '#'))
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day21.part_a(util.get_file_contents('day21.txt'))
        self.assertEqual(result, '173')

    '''
    --- No examples for part b ---

    @data(
        [],
        []
        )
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day21.part_b(test_input)
        self.assertEqual(result, expected)'''

    def test_answer_part_b(self): # noqa D102
        result = day21.part_b(util.get_file_contents('day21.txt'))
        self.assertEqual(result, '2456178')
