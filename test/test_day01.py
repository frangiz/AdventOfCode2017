from days import day01
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data(
        [['1122'], '3'],
        [['1111'], '4'],
        [['1234'], '0'],
        [['91212129'], '9']
        )
    @unpack
    def test_example_a(self, test_input, expected):
        result = day01.part_a(test_input)
        self.assertEqual(result, expected)

    @data(
        [['1212'], '6'],
        [['1221'], '0'],
        [['123425'], '4'],
        [['123123'], '12'],
        [['12131415'], '4']
        )
    @unpack
    def test_example_b(self, test_input, expected):
        result = day01.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day01.part_a(util.get_file_contents('day01.txt'))
        self.assertEqual(result, '1044')

    def test_answer_part_b(self):
        result = day01.part_b(util.get_file_contents('day01.txt'))
        self.assertEqual(result, '1054')
