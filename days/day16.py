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
    return registers


def promenade(puzzle_input, registers, iterations):
    visited_states = []
    index = 0
    while index < iterations:
        # A state that we already visited indicates that we have a loop.
        state = ''.join(registers)
        if state in visited_states:
            state_index = visited_states.index(state)
            loop_length = len(visited_states) - state_index
            offset = (iterations - index) % loop_length
            return visited_states[state_index + offset]
        visited_states.append(state)
        # Let's dance!
        registers = dance_once(puzzle_input, registers)
        index += 1
    return ''.join(registers)


def part_a(puzzle_input):
    registers = [c for c in 'abcdefghijklmnop']
    return promenade(puzzle_input, registers, 1)


def part_b(puzzle_input):
    registers = [c for c in 'abcdefghijklmnop']
    return promenade(puzzle_input, registers, 1000000000)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
