"""The tests for day19."""
from days import day19
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data([['     |          ',
            '     |  +--+    ',
            '     A  |  C    ',
            ' F---|----E|--+ ',
            '     |  |  |  D ',
            '     +B-+  +--+'], 'ABCDEF'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day19.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day19.part_a(util.get_file_contents('day19.txt'))
        self.assertEqual(result, 'FEZDNIVJWT')

    @data([['     |          ',
            '     |  +--+    ',
            '     A  |  C    ',
            ' F---|----E|--+ ',
            '     |  |  |  D ',
            '     +B-+  +--+'], '38'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day19.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day19.part_b(util.get_file_contents('day19.txt'))
        self.assertEqual(result, '17200')
