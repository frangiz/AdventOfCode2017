"""--- Day 17: Spinlock ---"""


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    We need to build a list since we do not know where 2017 will end up.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    steps = int(''.join(puzzle_input))
    numbers = [0]
    index = 0
    for i in range(1, 2017 + 1):
        index = (index + steps) % i
        numbers.insert(index + 1, i)
        index += 1
    return str(numbers[numbers.index(2017) + 1])


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    No need for a list since we only need to keep track of the latest number
    "written" when we are at index 0. This will speed up the calcuations... a lot!

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    steps = int(''.join(puzzle_input))
    index = 0
    n = 0
    for i in range(1, 50000001):
        index = (index + steps) % i
        if index == 0:
            n = i
        index += 1
    return str(n)


def solve(puzzle_input): # noqa D103
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
