def part_a(puzzle_input):
    values = []
    for line in puzzle_input:
        values.append(int(line.split()[4]))
    factors = [16807, 48271]
    matches = 0
    mask = (1 << 16) - 1
    for _ in range(40000000):
        values[0] = (values[0] * factors[0]) % 2147483647
        values[1] = (values[1] * factors[1]) % 2147483647
        if (values[0] & mask) == (values[1] & mask):
            matches += 1
    return str(matches)


def part_b(puzzle_input):
    values = []
    for line in puzzle_input:
        values.append(int(line.split()[4]))
    factors = [16807, 48271]
    compa = []
    compb = []
    while (len(compa) < 5000000 or len(compb) < 5000000):
        values[0] = (values[0] * factors[0]) % 2147483647
        values[1] = (values[1] * factors[1]) % 2147483647
        if values[0] % 4 == 0:
            compa.append(values[0])
        if values[1] % 8 == 0:
            compb.append(values[1])

    matches = 0
    mask = (1 << 16) - 1
    for i in range(5000000):
        if (compa[i] & mask) == (compb[i] & mask):
            matches += 1
    return str(matches)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
