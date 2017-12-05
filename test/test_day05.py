from days import day05
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data(
        [['0', '3', '0', '1', '-3'], '5']
        )
    @unpack
    def test_example_a(self, test_input, expected):
        result = day05.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day05.part_a(util.get_file_contents('day05.txt'))
        self.assertEqual(result, '372671')

    @data(
        [['0', '3', '0', '1', '-3'], '10']
        )
    @unpack
    def test_example_b(self, test_input, expected):
        result = day05.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day05.part_b(util.get_file_contents('day05.txt'))
        self.assertEqual(result, '25608480')