def part_a(puzzle_input):
    res = 0
    for line in puzzle_input:
        words = line.split()
        if len(words) == len(set(words)):
            res += 1
    return str(res)


def part_b(puzzle_input):
    res = 0
    for line in puzzle_input:
        words = [''.join(sorted(word)) for word in line.split()]
        if len(words) == len(set(words)):
            res += 1
    return str(res)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
