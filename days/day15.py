def part_a(puzzle_input):
    val_a, val_b = [int(line.split()[4]) for line in puzzle_input]
    factor_a, factor_b = [16807, 48271]
    matches = 0
    mask = (1 << 16) - 1
    for _ in range(40000000):
        val_a = (val_a * factor_a) % 2147483647
        val_b = (val_b * factor_b) % 2147483647
        if val_a & mask == val_b & mask:
            matches += 1
    return str(matches)


def part_b(puzzle_input):
    val_a, val_b = [int(line.split()[4]) for line in puzzle_input]
    factor_a, factor_b = [16807, 48271]
    matches = 0
    mask = (1 << 16) - 1
    for _ in range(5000000):
        comp_a = True
        comp_b = True
        while comp_a:
            val_a = (val_a * factor_a) % 2147483647
            comp_a = val_a % 4 != 0
        while comp_b:
            val_b = (val_b * factor_b) % 2147483647
            comp_b = val_b % 8 != 0
        if val_a & mask == val_b & mask:
            matches += 1
    return str(matches)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
