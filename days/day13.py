def cross_firewall(scanners, offset=0, break_caught=False):
    sev = 0
    for pos, depth in scanners.items():
        if (pos + offset) % ((depth - 1) * 2) == 0:
            sev += pos * depth
            if break_caught:
                return (True, sev)
    return (False, sev)


def parse_input(puzzle_input):
    return { int(key): int(value) for key, value in (line.split(':') for line in puzzle_input) }


def part_a(puzzle_input):
    scanners = parse_input(puzzle_input)
    return str(cross_firewall(scanners)[1])


def part_b(puzzle_input):
    scanners = parse_input(puzzle_input)
    for i in range(10**10):
        caught, sev = cross_firewall(scanners, i, True)
        if not caught:
            return str(i)
    return str(0)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
