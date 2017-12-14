from collections import deque
from days import day10


def get_grid(puzzle_input):
    grid = []
    prefix = ''.join(puzzle_input).strip() + '-'
    for i in range(128):
        kh = day10.KnotHash(256)
        bin_str = '{:0128b}'.format(int(kh.calc_hash(prefix + str(i)), 16))
        grid.append(bin_str)
    return grid


def part_a(puzzle_input):
    grid = get_grid(puzzle_input)
    n = 0
    for line in grid:
        n += sum(1 for char in line if char == '1')
    return str(n)


def part_b(puzzle_input):
    grid = get_grid(puzzle_input)
    regions = 0
    visited = set()
    for line in range(128):
        for col in range(128):
            if grid[line][col] == '0':
                continue
            elif (line, col) in visited:
                continue
            regions += 1
            neighbours = deque()
            neighbours.append((line, col))
            while neighbours:
                y, x = neighbours.pop()
                if (y, x) in visited:
                    continue
                if grid[y][x] == '0':
                    continue
                visited.add((y, x))
                if y > 0:
                    neighbours.append((y - 1, x))
                if y < 127:
                    neighbours.append((y + 1, x))
                if x < 127:
                    neighbours.append((y, x + 1))
                if x > 0:
                    neighbours.append((y, x - 1))
    return str(regions)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
