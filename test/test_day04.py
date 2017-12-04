from days import day04
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data(
        [['aa bb cc dd ee', 'aa bb cc dd aa', 'aa bb cc dd aaa'], '2']
        )
    @unpack
    def test_example_a(self, test_input, expected):
        result = day04.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day04.part_a(util.get_file_contents('day04.txt'))
        self.assertEqual(result, '383')

    @data(
        [['abcde fghij'], '1'],
        [['abcde xyz ecdab'], '0'],
        [['a ab abc abd abf abj'], '1'],
        [['iiii oiii ooii oooi oooo'], '1'],
        [['oiii ioii iioi iiio'], '0'],
        )
    @unpack
    def test_example_b(self, test_input, expected):
        result = day04.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day04.part_b(util.get_file_contents('day04.txt'))
        self.assertEqual(result, '265')