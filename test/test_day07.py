from days import day07
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data(
        [[
            'pbga (66)',
            'xhth (57)',
            'ebii (61)',
            'havc (66)',
            'ktlj (57)',
            'fwft (72) -> ktlj, cntj, xhth',
            'qoyq (66)',
            'padx (45) -> pbga, havc, qoyq',
            'tknk (41) -> ugml, padx, fwft',
            'jptl (61)',
            'ugml (68) -> gyxo, ebii, jptl',
            'gyxo (61)',
            'cntj (57)'], 'tknk'])
    @unpack
    def test_example_a(self, test_input, expected):
        result = day07.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day07.part_a(util.get_file_contents('day07.txt'))
        self.assertEqual(result, 'fbgguv')

    @data(
        [[
            'pbga (66)',
            'xhth (57)',
            'ebii (61)',
            'havc (66)',
            'ktlj (57)',
            'fwft (72) -> ktlj, cntj, xhth',
            'qoyq (66)',
            'padx (45) -> pbga, havc, qoyq',
            'tknk (41) -> ugml, padx, fwft',
            'jptl (61)',
            'ugml (68) -> gyxo, ebii, jptl',
            'gyxo (61)',
            'cntj (57)'], '60'])
    @unpack
    def test_example_b(self, test_input, expected):
        result = day07.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day07.part_b(util.get_file_contents('day07.txt'))
        self.assertEqual(result, '1864')
