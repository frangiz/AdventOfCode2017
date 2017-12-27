"""--- Day 25: The Halting Problem ---"""
from collections import namedtuple, defaultdict
import re

# Really waiting for https://www.python.org/dev/peps/pep-0557/
Transition = namedtuple('Transition', 'state trigger_value write_value index_offset next_state')


class TuringMachine:
    """The awesome turing machine."""

    def __init__(self, puzzle_input):
        """ctor, nothing more exiting."""
        self.curr_state = ''
        self.steps = 0
        self.transitions = self._parse_transitions(puzzle_input)
        self.tape = defaultdict(int)

    def _parse_transitions(self, puzzle_input):
        """
        Parse transitions.

        Args:
            puzzle_input (list): Formatted as the provided input from the website.
        Returns
            dict: A dictionary of Transition.

        """
        state = ''
        trigger_value = -1
        write_value = -1
        index_offset = 0
        next_state = ''
        transitions = {}
        for line in puzzle_input:
            m = re.search('Begin in state ([a-zA-Z]+)\.', line)
            if m is not None:
                self.curr_state = m.group(1)
                continue
            m = re.search('Perform a diagnostic checksum after (\d+) steps\.', line)
            if m is not None:
                self.steps = int(m.group(1))
                continue
            m = re.search('In state ([a-zA-Z]+):', line)
            if m is not None:
                state = m.group(1)
                continue
            m = re.search('If the current value is (\d+):', line)
            if m is not None:
                trigger_value = int(m.group(1))
                continue
            m = re.search('Write the value (\d+).', line)
            if m is not None:
                write_value = int(m.group(1))
                continue
            m = re.search('Move one slot to the (right|left).', line)
            if m is not None:
                index_offset = 1 if m.group(1) == 'right' else -1
                continue
            m = re.search('Continue with state ([a-zA-Z]+)\.', line)
            if m is not None:
                next_state = m.group(1)
                transitions[(state, trigger_value)] = Transition(
                    state, trigger_value, write_value, index_offset, next_state)
        return transitions

    def run_diagnostics(self):
        """
        Run diagnostic.

        Runs a diagnostic according to the parsed transitions. Writes a 0 or 1
        to the self.tape dictionary.
        """
        cursor = 0
        for _ in range(self.steps):
            transition = self.transitions[(self.curr_state, self.tape[cursor])]
            self.tape[cursor] = transition.write_value
            cursor += transition.index_offset
            self.curr_state = transition.next_state


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    turing_machine = TuringMachine(puzzle_input)
    turing_machine.run_diagnostics()
    return str(sum(v for k, v in turing_machine.tape.items()))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
