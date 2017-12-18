"""--- Day 18: Duet ---"""
from collections import defaultdict, deque


class Tablet:
    """A tablet represenatation able to run the assembly code Duet."""

    def __init__(self, puzzle_input, send_queue, receive_queue):
        """ctor, nothing more exiting."""
        self.instructions = puzzle_input
        self.send_queue = send_queue
        self.receive_queue = receive_queue
        self.registers = defaultdict(int)
        self.pc = 0
        self.send_counter = 0

    def step(self):
        """
        Execute the next instruction and move the pc counter to the next instruction.

        Returns:
            bool: True if the currect instruction could be executed.
                    False if an 'rcv' instruction is called and self.receive_queue
                    is empty.
        Throws:
            Exception: If the instruction is unknown and cannot be handled or if
                        self.pc points to an invalid index of self.instructions.

        """
        if self.pc < 0 or self.pc >= len(self.instructions):
            raise Exception('Index out of bounds for pc.')
        ins, x, *optionals = self.instructions[self.pc].split()
        y = optionals[0] if len(optionals) > 0 else None
        if ins == 'snd':
            self.send_counter += 1
            self.send_queue.append(self._get_value(x))
        elif ins == 'set':
            self.registers[x] = self._get_value(y)
        elif ins == 'add':
            self.registers[x] += self._get_value(y)
        elif ins == 'mul':
            self.registers[x] *= self._get_value(y)
        elif ins == 'mod':
            self.registers[x] %= self._get_value(y)
        elif ins == 'rcv':
            if not self.receive_queue:
                return False
            self.registers[x] = self.receive_queue.popleft()
        elif ins == 'jgz':
            if self._get_value(x) > 0:
                # -1 since we always add 1 to self.pc later in the method.
                self.pc += self._get_value(y) - 1
        else:
            raise Exception('Unable to parse instruction: ' + self.instructions[self.pc])
        self.pc += 1
        return True

    def _get_value(self, value):
        """Convert the value into an int or return value of self.registers[value]."""
        try:
            return int(value)
        except ValueError:
            return self.registers[value]


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    send_queue = deque()
    t = Tablet(puzzle_input, send_queue, deque())
    while True:
        if not t.step():
            break
    return str(send_queue.pop())


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    q0 = deque()
    q1 = deque()
    t0 = Tablet(puzzle_input, q0, q1)
    t1 = Tablet(puzzle_input, q1, q0)
    t1.registers['p'] = 1
    while True:
        if not t0.step() and not t1.step():
            break
    return str(t1.send_counter)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
