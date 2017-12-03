def part_a(input):
    input_str = ''.join(input)
    chars = len(input_str)
    return str(sum(int(c) for i, c in enumerate(input_str) if c == input_str[(i + 1) % chars]))


def part_b(input):
    input_str = ''.join(input)
    res = 0
    chars = len(input_str)
    for i, c in enumerate(input_str[:chars // 2]):
        if c == input_str[i + chars // 2]:
            res += int(c) * 2
    return str(res)


def solve(input):
    return {'a': part_a(input), 'b': part_b(input)}
