def part_a(input):
    res = 0
    for line in input:
        words = line.split()
        if len(words) == len(set(words)):
            res += 1
    return str(res)


def part_b(input):
    res = 0
    for line in input:
        words = [''.join(sorted(word)) for word in line.split()]
        if len(words) == len(set(words)):
            res += 1
    return str(res)


def solve(input):
    return {'a': part_a(input), 'b': part_b(input)}
