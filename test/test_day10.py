from days import day10
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data([['3, 4, 1, 5'], 12])
    @unpack
    def test_example_a(self, test_input, expected):
        kh = day10.KnotHash(5)
        kh.knot_hash(list(map(int, ''.join(test_input).split(','))))
        result = kh.registers[0] * kh.registers[1]
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day10.part_a(util.get_file_contents('day10.txt'))
        self.assertEqual(result, '29240')

    @data(
        [[''], 'a2582a3a0e66e6e86e3812dcb672a272'],
        [['AoC 2017'], '33efeb34ea91902bb2f59c9920caa6cd'],
        [['1,2,3'], '3efbe78a8d82f29979031a4aa0b16a9d'],
        [['1,2,4'], '63960835bcdc130f0b66d7ff4f6a5a8e'])
    @unpack
    def test_example_b(self, test_input, expected):
        result = day10.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day10.part_b(util.get_file_contents('day10.txt'))
        self.assertEqual(result, '4db3799145278dc9f73dcdbc680bd53d')
