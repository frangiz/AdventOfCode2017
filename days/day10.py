def knot_hash(num_registers, lengths):
    registers = [i for i in range(num_registers)]
    index = 0
    skip = 0
    lengths = list(map(int, ''.join(lengths).split(',')))
    for length in lengths:
        if length > len(registers):
            continue
        # collect items
        items = registers[index:length + index]
        if len(items) < length:
            items += registers[0:length - len(items)]
        # reverse them
        items.reverse()
        for i in range(len(items)):
            registers[(i + index) % len(registers)] = items[i]
        index = (index + length + skip) % num_registers
        skip += 1
    return registers[0] * registers[1]


def part_a(puzzle_input):
    return str(knot_hash(256, puzzle_input))


def part_b(puzzle_input):
    return str(0)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
