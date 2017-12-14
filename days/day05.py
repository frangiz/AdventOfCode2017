def part_a(puzzle_input):
    input_ints = [int(i) for i in puzzle_input]
    index = 0
    steps = 0
    len_input = len(input_ints)
    while index >= 0 and index < len_input:
        new_index = input_ints[index] + index
        input_ints[index] += 1
        index = new_index
        steps += 1
    return str(steps)


def part_b(puzzle_input):
    input_ints = [int(i) for i in puzzle_input]
    index = 0
    steps = 0
    len_input = len(input_ints)
    while index >= 0 and index < len_input:
        new_index = input_ints[index] + index
        input_ints[index] += 1 if input_ints[index] < 3 else - 1
        index = new_index
        steps += 1
    return str(steps)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
