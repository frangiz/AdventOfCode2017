"""The tests for day18."""
from days import day18
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['set a 1',
            'add a 2',
            'mul a a',
            'mod a 5',
            'snd a',
            'set a 0',
            'rcv a',
            'jgz a -1',
            'set a 1',
            'jgz a -2'], '4'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day18.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day18.part_a(util.get_file_contents('day18.txt'))
        self.assertEqual(result, '8600')

    @data(
        [['snd 1',
            'snd 2',
            'snd p',
            'rcv a',
            'rcv b',
            'rcv c',
            'rcv d'], '3'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day18.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day18.part_b(util.get_file_contents('day18.txt'))
        self.assertEqual(result, '7239')
