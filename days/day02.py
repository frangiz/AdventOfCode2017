from itertools import combinations


def part_a(puzzle_input):
    sums = 0
    for line in puzzle_input:
        values = [int(i) for i in line.split()]
        sums += max(values) - min(values)
    return str(sums)


def part_b(puzzle_input):
    result = 0
    for line in puzzle_input:
        values = [int(i) for i in line.split()]
        for n1, n2 in combinations(values, 2):
            if (n1 / n2).is_integer():
                result += n1 // n2
            elif (n2 / n1).is_integer():
                result += n2 // n1
    return str(result)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
