"""--- Day 21: Fractal Art ---"""
import numpy as np


def parse_rules(puzzle_input):
    """
    Parses the puzzle_input and coverts it to a set of convert rules.

    The method handles all rotations and the corresponding flips of all rules.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        dict: The convert rules.

    """
    patterns = {}
    for line in puzzle_input:
        inp, out = line.split(' => ')
        key_arr = np.array([[c for c in l] for l in inp.split('/')])
        val = tuple(out.strip().split('/'))
        flipped = np.fliplr(key_arr)

        for _ in range(4):
            patterns[tuple(''.join(row) for row in key_arr)] = val
            patterns[tuple(''.join(row) for row in flipped)] = val
            key_arr = np.rot90(key_arr)
            flipped = np.rot90(flipped)
    return patterns


def expand(rules, input_grid, iterations):
    """
    Expands the grid the number of iterations according to the rules.

    Args:
        rules (dict): Formatted as the output from parse_rules.
        input_grid (list): Base grid formatted as a tuple of strings.
        iterations (int): The number of iterations to apply the rules to the grid.
    Returns:
        list: The new grid as a list of strings.

    """
    current_grid = input_grid
    for _ in range(iterations):
        new_size = len(current_grid) // 2 * 3 if len(current_grid) % 2 == 0 else len(current_grid) // 3 * 4
        new_grid = ['' for _ in range(new_size)]
        if len(current_grid) % 2 == 0:
            # walk a block of 2x2 at a time
            for line in range(0, len(current_grid), 2):
                for col in range(0, len(current_grid), 2):
                    key = tuple([
                        ''.join(current_grid[line][col:col + 2]),
                        ''.join(current_grid[line + 1][col:col + 2])])
                    new_block = rules[key]
                    for i, block_line in enumerate(new_block):
                        new_grid[line // 2 * 3 + i] += block_line
        elif len(current_grid) % 3 == 0:
            # walk a block of 3x3 at a time
            for line in range(0, len(current_grid), 3):
                for col in range(0, len(current_grid), 3):
                    key = tuple([
                        ''.join(current_grid[line][col:col + 3]),
                        ''.join(current_grid[line + 1][col:col + 3]),
                        ''.join(current_grid[line + 2][col:col + 3])])
                    new_block = rules[key]
                    for i, block_line in enumerate(new_block):
                        new_grid[line // 3 * 4 + i] += block_line
        current_grid = new_grid
    return current_grid


def count(grid, char):
    """Counts the occurrences of [char] in the grid."""
    res = 0
    for line in grid:
        res += sum(1 for c in line if c == char)
    return res


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    rules = parse_rules(puzzle_input)
    start_grid = ('.#.', '..#', '###')
    new_grid = expand(rules, start_grid, 5)
    return str(count(new_grid, '#'))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    rules = parse_rules(puzzle_input)
    start_grid = ('.#.', '..#', '###')
    new_grid = expand(rules, start_grid, 18)
    return str(count(new_grid, '#'))


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
