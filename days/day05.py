def part_a(input):
    input_ints = [int(i) for i in input]
    index = 0
    steps = 0
    while index >= 0 and index < len(input_ints):
        new_index = input_ints[index] + index
        input_ints[index] += 1
        index = new_index
        steps += 1
    return str(steps)


def part_b(input):
    input_ints = [int(i) for i in input]
    index = 0
    steps = 0
    while index >= 0 and index < len(input_ints):
        new_index = input_ints[index] + index
        input_ints[index] += 1 if input_ints[index] < 3 else - 1
        index = new_index
        steps += 1
    return str(steps)


def solve(input):
    return {'a': part_a(input), 'b': part_b(input)}
