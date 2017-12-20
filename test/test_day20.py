"""The tests for day20."""
from days import day20
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data([['p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>',
            'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>'], '0'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day20.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day20.part_a(util.get_file_contents('day20.txt'))
        self.assertEqual(result, '300')

    @data([['p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>',
            'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>',
            'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>',
            'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>'], '1'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day20.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day20.part_b(util.get_file_contents('day20.txt'))
        self.assertEqual(result, '502')
