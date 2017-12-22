"""--- Day 16: Permutation Promenade ---"""


def dance_once(puzzle_input, programs):
    """
    Do one full round of the dance according to the puzzle_input.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
        programs (list): The programs that will dance.
    Returns:
        list: The new order of the programs.
    Examples:
        >>> dance_once(['s1,x3/4,pe/b'], [c for c in 'abcde'])
        ['b', 'a', 'e', 'd', 'c']

    """
    for dance_move in ''.join(puzzle_input).split(','):
        if dance_move.startswith('s'):
            spin = int(dance_move[1:])
            programs = programs[-spin:] + programs[:-spin]
        elif dance_move.startswith('x'):
            a, b = map(int, dance_move[1:].split('/'))
            programs[a], programs[b] = programs[b], programs[a]
        elif dance_move.startswith('p'):
            a, b = dance_move[1:].split('/')
            index_a = programs.index(a)
            index_b = programs.index(b)
            programs[index_a], programs[index_b] = programs[index_b], programs[index_a]
    return programs


def dance(puzzle_input, programs, iterations):
    """
    Dancing the programs the number of iterations. Can detect loops!

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
        programs (list): The programs that will dance.
        iterations (int): The number of iterations to dance.
    Returns:
        string: The result of dancing n number of iterations.

    """
    visited_states = []
    index = 0
    while index < iterations:
        # A state that we already visited indicates that we have a loop.
        state = ''.join(programs)
        if state in visited_states:
            state_index = visited_states.index(state)
            loop_length = len(visited_states) - state_index
            offset = (iterations - index) % loop_length
            return visited_states[state_index + offset]
        visited_states.append(state)
        # Let's dance!
        programs = dance_once(puzzle_input, programs)
        index += 1
    return ''.join(programs)


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    registers = [c for c in 'abcdefghijklmnop']
    return dance(puzzle_input, registers, 1)


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    registers = [c for c in 'abcdefghijklmnop']
    return dance(puzzle_input, registers, 1000000000)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
