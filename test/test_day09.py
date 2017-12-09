from days import day09
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data(
        [['{}'], '1'],
        [['{{{}}}'], '6'],
        [['{{},{}}'], '5'],
        [['{{{},{},{{}}}}'], '16'],
        [['{<a>,<a>,<a>,<a>}'], '1'],
        [['{{<ab>},{<ab>},{<ab>},{<ab>}}'], '9'],
        [['{{<!!>},{<!!>},{<!!>},{<!!>}}'], '9'],
        [['{{<a!>},{<a!>},{<a!>},{<ab>}}'], '3'])
    @unpack
    def test_example_a(self, test_input, expected):
        result = day09.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day09.part_a(util.get_file_contents('day09.txt'))
        self.assertEqual(result, '14190')

    @data(
        [['<>'], '0'],
        [['<random characters>'], '17'],
        [['<<<<>'], '3'],
        [['<{!>}>'], '2'],
        [['<!!>'], '0'],
        [['<!!!>>'], '0'],
        [['<{o"i!a,<{i<a>'], '10'])
    @unpack
    def test_example_b(self, test_input, expected):
        result = day09.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day09.part_b(util.get_file_contents('day09.txt'))
        self.assertEqual(result, '7053')
