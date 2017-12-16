def dance_once(puzzle_input, registers):
    for dance_move in ''.join(puzzle_input).split(','):
        if dance_move.startswith('s'):
            spin = int(dance_move[1:])
            registers = registers[-spin:] + registers[:-spin]
        elif dance_move.startswith('x'):
            a, b = map(int, dance_move[1:].split('/'))
            registers[a], registers[b] = registers[b], registers[a]
        elif dance_move.startswith('p'):
            a, b = dance_move[1:].split('/')
            index_a = registers.index(a)
            index_b = registers.index(b)
            registers[index_a], registers[index_b] = registers[index_b], registers[index_a]
    return ''.join(registers)


def promenade(puzzle_input, registers, iterations):
    substitutions = {}
    index = 0
    state = ''.join(registers)
    while index < iterations:
        if state in substitutions:
            state = substitutions[state]
        else:
            new_state = ''.join(dance_once(puzzle_input, list(state)))
            substitutions[state] = new_state
            state = new_state
        index += 1
    return state


def part_a(puzzle_input):
    registers = [chr(i) for i in range(97, 113)]
    return promenade(puzzle_input, registers, 1)


def part_b(puzzle_input):
    registers = [chr(i) for i in range(97, 113)]
    return promenade(puzzle_input, registers, 1000000000)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
