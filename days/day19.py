"""--- Day 19: A Series of Tubes ---"""


def collect_letters(grid):
    """
    Collect the letters along a path.

    The algorithm is quite stupid. It handles branching by changing the direction
    it has, e.g. walking down to a branch where it is possible to move down and
    left, will result in left.

    Args:
        grid (list): Formatted as the provided input from the website.
    Returs:
        Tuple: First value in the tuple is the letters and the second value
                holds the number of steps taken.
    """
    x = grid[0].index('|')
    y = 0
    letters = []
    direction = 'D'
    steps = 0
    while grid[y][x] != ' ':
        # step
        if direction == 'D':
            y += 1
        elif direction == 'U':
            y -= 1
        elif direction == 'L':
            x -= 1
        elif direction == 'R':
            x += 1
        steps += 1
        # collect the letter if we are standing in a letter
        if grid[y][x].isalpha():
            letters.append(grid[y][x])
        # we assume that when we find a '+', we will turn and not continue
        # in the same direction.
        elif grid[y][x] == '+':
            if direction in ['U', 'D']:
                if can_move(grid, x - 1, y):
                    direction = 'L'
                elif can_move(grid, x + 1, y):
                    direction = 'R'
            else:
                if can_move(grid, x, y - 1):
                    direction = 'U'
                elif can_move(grid, x, y + 1):
                    direction = 'D'
    return (letters, steps)


def can_move(grid, x, y):
    return x >= 0 and x < len(grid[y]) and y >= 0 and y < len(grid) and grid[y][x] != ' '


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    return ''.join(collect_letters(puzzle_input)[0])


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    return str(collect_letters(puzzle_input)[1])


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
