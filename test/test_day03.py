from days import day03
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data(
        [['1'], '0'],
        [['12'], '3'],
        [['23'], '2'],
        [['1024'], '31'],
        [['41'], '4'],
        [['63'], '6']
        )
    @unpack
    def test_example_a(self, test_input, expected):
        result = day03.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day03.part_a(util.get_file_contents('day03.txt'))
        self.assertEqual(result, '371')

    @data(
        [['2'], '4'],
        [['7'], '10'],
        [['123'], '133'],
        [['805'], '806']
        )
    @unpack
    def test_example_b(self, test_input, expected):
        result = day03.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day03.part_b(util.get_file_contents('day03.txt'))
        self.assertEqual(result, '369601')
