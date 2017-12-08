from collections import defaultdict


class Computer:
    def __init__(self):
        self.registers = defaultdict(lambda: 0)
        self.highest_value = 0

    def run(self, puzzle_input):
        for line in puzzle_input:
            action, condition = line.split('if')
            if self.eval_condition(condition):
                self.eval_action(action)

    def eval_condition(self, condition):
        parts = condition.split()
        cond = 'self.registers[\'{0}\'] {1}'.format(parts[0], ' '.join(parts[1:]))
        return eval(cond)

    def eval_action(self, action):
        reg, op, val = action.split()
        if op == 'inc':
            self.registers[reg] += int(val)
        elif op == 'dec':
            self.registers[reg] -= int(val)
        self.highest_value = max(self.highest_value, self.registers[reg])


def part_a(puzzle_input):
    c = Computer()
    c.run(puzzle_input)
    return str(c.registers[max(c.registers, key=lambda k: c.registers[k])])


def part_b(puzzle_input):
    c = Computer()
    c.run(puzzle_input)
    return str(c.highest_value)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
