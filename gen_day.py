import argparse
import glob
import os

day_template = """def part_a(input):
    return str(0)


def part_b(input):
    return str(0)


def solve(input):
    return {'a': part_a(input), 'b': part_b(input)}
"""

test_day_template = """from days import day{0}
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase):
    @data(
        [],
        []
        )
    @unpack
    def test_example_a(self, test_input, expected):
        result = day{0}.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self):
        result = day{0}.part_a(util.get_file_contents('day{0}.txt'))
        self.assertEqual(result, '')

    @data(
        [],
        []
        )
    @unpack
    def test_example_b(self, test_input, expected):
        result = day{0}.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self):
        result = day{0}.part_b(util.get_file_contents('day{0}.txt'))
        self.assertEqual(result, '')
"""


def regenerate_days_init_file():
    number_of_days = len(glob.glob('days/day*'))
    days = ['\"day{num:02d}\"'.format(num=day) for day in range(1, number_of_days + 1)]
    unwrapped_contents = '__all__ = [\t{0}]'.format(', '.join(days))
    with open('days/__init__.py', 'w') as f:
        f.write(unwrapped_contents)


def create_files_for_day(day):
    if not os.path.isfile('days/day' + day + '.py'):
        with open('days/day' + day + '.py', 'w') as f:
            f.writelines(day_template)
    if not os.path.isfile('test/test_day' + day + '.py'):
        with open('test/test_day' + day + '.py', 'w') as f:
            f.writelines(test_day_template.format(day))
    if not os.path.isfile('inputs/day' + day + '.txt'):
        with open('inputs/day' + day + '.txt', 'w') as f:
            pass
    regenerate_days_init_file()


def main():
    parser = argparse.ArgumentParser(prog='Generate Day')
    parser.add_argument('-d', '--day', type=str, help='The day to create files for.')
    args = parser.parse_args()

    if args.day is not None:
        create_files_for_day(args.day)


if __name__ == '__main__':
    main()
