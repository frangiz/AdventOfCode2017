def part_a(input):
    input_str = ''.join(input)
    res = 0
    for i, c in enumerate(input_str[:-1]):
        if c == input_str[i+1]:
            res += int(c)
    res += int(input_str[0]) if input_str[0] == input_str[-1] else 0
    return str(res)


def part_b(input):
    input_str = ''.join(input)
    res = 0
    for i, c in enumerate(input_str):
        if c == input_str[int((len(input_str) / 2 + i) % len(input_str))]:
            res += int(c)
    return str(res)


def solve(input):
    return {'a': part_a(input), 'b': part_b(input)}
