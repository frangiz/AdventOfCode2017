def calc(chars):
    tot_score = 0
    score_stack = []
    curr_score = 0
    index = 0
    garbage = False
    garbage_count = 0
    while index < len(chars):
        if chars[index] == '!':
            index += 1
        elif garbage and chars[index] != '>':
            garbage_count += 1
        elif chars[index] == '>':
            garbage = False
        elif chars[index] == '<':
            garbage = True
        elif chars[index] == '{':
            curr_score += 1
            score_stack.append(curr_score)
        elif chars[index] == '}':
            curr_score -= 1
            tot_score += score_stack.pop()
        index += 1
    return (tot_score, garbage_count)


def part_a(puzzle_input):
    return str(calc(''.join(puzzle_input))[0])


def part_b(puzzle_input):
    return str(calc(''.join(puzzle_input))[1])


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
