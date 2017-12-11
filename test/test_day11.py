from days import day11
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data(
        [['ne,ne,ne'], '3'],
        [['ne,ne,sw,sw'], '0'],
        [['ne,ne,s,s'], '2'],
        [['se,sw,se,sw,sw'], '3'])
    @unpack
    def test_example_a(self, test_input, expected):
        result = day11.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day11.part_a(util.get_file_contents('day11.txt'))
        self.assertEqual(result, '812')

    @data([['n,n,n,s,s'], '3'])
    @unpack
    def test_example_b(self, test_input, expected):
        result = day11.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day11.part_b(util.get_file_contents('day11.txt'))
        self.assertEqual(result, '1603')
