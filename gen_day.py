import os

day_template = """def part_a(puzzle_input):
    return str(0)


def part_b(puzzle_input):
    return str(0)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
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


def regenerate_days_init_file(day):
    number_of_days = int(day)
    days = ['\"day{num:02d}\"'.format(num=day) for day in range(1, number_of_days + 1)]
    day_lines = [days[i * 7: i * 7 + 7] for i in range(number_of_days // 7 + 1)]
    day_lines = [day_lines[i] for i in range(len(day_lines)) if len(day_lines[i]) > 0]
    text = '__all__ = [ '
    text += ', '.join(day_lines[0])
    if len(day_lines) > 1:
        for line in day_lines[1:]:
            text += ',\n' + (' ' * 12) + ', '.join(line)
    text += ']'

    with open('days/__init__.py', 'w') as f:
        f.write(text)


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
    regenerate_days_init_file(day)


def find_day_to_genrerate():
    files = len(os.listdir('inputs'))
    if files <= 24:  # 25 puzzle days for AoC
        return '{0:02d}'.format(files + 1)
    else:
        return None


def main():
    day = find_day_to_genrerate()
    if day is not None:
        create_files_for_day(day)
    else:
        print('Max number of days created.')


if __name__ == '__main__':
    main()
