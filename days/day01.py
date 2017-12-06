def part_a(puzzle_input):
    input_str = ''.join(puzzle_input)
    chars = len(input_str)
    return str(sum(int(c) for i, c in enumerate(input_str) if c == input_str[(i + 1) % chars]))


def part_b(puzzle_input):
    input_str = ''.join(puzzle_input)
    res = 0
    chars = len(input_str)
    for i, c in enumerate(input_str[:chars // 2]):
        if c == input_str[i + chars // 2]:
            res += int(c) * 2
    return str(res)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
