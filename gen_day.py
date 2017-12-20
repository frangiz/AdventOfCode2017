"""Generates the files needed for the next day."""
import os

day_template = """\"\"\"--- Day {0}: Dayname ---\"\"\"


def part_a(puzzle_input):
    \"\"\"
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    \"\"\"
    return str(0)


def part_b(puzzle_input):
    \"\"\"
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    \"\"\"
    return str(0)


def solve(puzzle_input):
    \"\"\"Returs the answer for both parts.\"\"\"
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
"""

test_day_template = """\"\"\"The tests for day{0}.\"\"\"
from days import day{0}
from ddt import ddt, data, unpack
import unittest
import util


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [],
        []
        )
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day{0}.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day{0}.part_a(util.get_file_contents('day{0}.txt'))
        self.assertEqual(result, '')

    @data(
        [],
        []
        )
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day{0}.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day{0}.part_b(util.get_file_contents('day{0}.txt'))
        self.assertEqual(result, '')
"""


def regenerate_days_init_file(number_of_days):
    """
    Renegerates the __init__.py file in the module days.

    The method have some logic to indent the list when it gets close to the
    80 charactes wide mark.

    Args:
        number_of_days (int): The number of days to be written to the file.
    """
    days = ['\"day{num:02d}\"'.format(num=day) for day in range(1, number_of_days + 1)]
    day_lines = [days[i * 7: i * 7 + 7] for i in range(number_of_days // 7 + 1)]
    day_lines = [day_lines[i] for i in range(len(day_lines)) if len(day_lines[i]) > 0]
    text = '__all__ = [ '
    text += ', '.join(day_lines[0]) + ' # noqa D104'
    if len(day_lines) > 1:
        for line in day_lines[1:]:
            text += ',\n' + (' ' * 12) + ', '.join(line)
    text += ']'

    with open('days/__init__.py', 'w') as f:
        f.write(text)
        f.write('\n')


def create_files(day):
    """
    Create the files needed for a new day.

    Each day needs three files.
        - days/day[n].py - The source code for the day.
        - test/test_day[n].py - The corresponding tests.
        - input/day[n].txt - The input formatted as the input from the website.
    Each day will also be appended to the __init__.py file for the module days.

    Args:
        day (string): The day to create formatted with two or more digits.

    """
    if not os.path.isfile('days/day' + day + '.py'):
        with open('days/day' + day + '.py', 'w') as f:
            f.writelines(day_template.format(day))
    if not os.path.isfile('test/test_day' + day + '.py'):
        with open('test/test_day' + day + '.py', 'w') as f:
            f.writelines(test_day_template.format(day))
    if not os.path.isfile('inputs/day' + day + '.txt'):
        with open('inputs/day' + day + '.txt', 'w') as f:
            pass
    regenerate_days_init_file(int(day))


def day_to_gen():
    """
    Return the day to generate in the inverval [1-25].

    Returns:
        string/None: A string formatted with two digits if the day is valid else None.

    """
    files = len(os.listdir('inputs'))
    if files <= 24:  # 25 puzzle days for AoC
        return '{0:02d}'.format(files + 1)
    else:
        return None


def main(): # noqa D103
    day = day_to_gen()
    if day is not None:
        create_files(day)
    else:
        print('Max number of days created.')


if __name__ == '__main__':
    main()
