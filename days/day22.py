"""--- Day 22: Sporifica Virus ---"""
from collections import defaultdict
from util import Point


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    visited = defaultdict(lambda: '.')
    # setup default grid
    for line in range(len(puzzle_input)):
        for col in range(len(puzzle_input[line])):
            visited[Point(col, line)] = puzzle_input[line][col]
    curr_pos = Point(len(puzzle_input) // 2, len(puzzle_input) // 2)
    curr_dir = Point(0, -1)  # facing up
    infected_counter = 0
    for _ in range(10000):
        # 1) wake up
        if visited[curr_pos] == '#':
            # turning right and cleaning
            curr_dir = Point(-curr_dir.y, curr_dir.x)
            del visited[curr_pos]
        else:
            # turning left and infecting
            curr_dir = Point(curr_dir.y, -curr_dir.x)
            infected_counter += 1
            visited[curr_pos] = '#'
        curr_pos = Point(curr_pos.x + curr_dir.x, curr_pos.y + curr_dir.y)
    return str(infected_counter)


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    visited = defaultdict(lambda: 'C')
    # setup default grid
    for line in range(len(puzzle_input)):
        for col in range(len(puzzle_input[line])):
            visited[Point(col, line)] = 'I' if puzzle_input[line][col] == '#' else 'C'
    curr_pos = Point(len(puzzle_input) // 2, len(puzzle_input) // 2)
    curr_dir = Point(0, -1)  # facing up
    infected_counter = 0
    for _ in range(10000000):
        if visited[curr_pos] == 'C':
            # turning left
            curr_dir = Point(curr_dir.y, -curr_dir.x)
            visited[curr_pos] = 'W'
        elif visited[curr_pos] == 'W':
            visited[curr_pos] = 'I'
            infected_counter += 1
        elif visited[curr_pos] == 'I':
            # turning right
            curr_dir = Point(-curr_dir.y, curr_dir.x)
            visited[curr_pos] = 'F'
        elif visited[curr_pos] == 'F':
            # U-turn
            curr_dir = Point(-curr_dir.x, -curr_dir.y)
            # no point in keep clean nodes
            del visited[curr_pos]
        curr_pos = Point(curr_pos.x + curr_dir.x, curr_pos.y + curr_dir.y)
    return str(infected_counter)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
