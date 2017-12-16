from days import day16
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data(
        [['s1'], 'eabcd'],
        [['s1,x3/4'], 'eabdc'],
        [['s1,x3/4,pe/b'], 'baedc'])
    @unpack
    def test_example_a(self, test_input, expected):
        registers = [c for c in 'abcde']
        result = day16.promenade(test_input, registers, 1)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day16.part_a(util.get_file_contents('day16.txt'))
        self.assertEqual(result, 'lgpkniodmjacfbeh')

    @data([['s1,x3/4,pe/b'], 'ceadb'])
    @unpack
    def test_example_b(self, test_input, expected):
        registers = [c for c in 'abcde']
        result = day16.promenade(test_input, registers, 2)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day16.part_b(util.get_file_contents('day16.txt'))
        self.assertEqual(result, 'hklecbpnjigoafmd')
