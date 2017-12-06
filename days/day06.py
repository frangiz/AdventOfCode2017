import operator


class MemoryReallocator:
    def __init__(self, input):
        self.banks = [int(i) for i in ''.join(input).split()]
        self.visited_states = {}
        self.cycles = 0
        self.last_state = ''

    def reallocate(self):
        done = False
        while not done:
            index, val = max(enumerate(self.banks), key=operator.itemgetter(1))
            self.banks[index] = 0
            for offset in range(val):
                self.banks[(index + offset + 1) % len(self.banks)] += 1
            self.last_state = str(self.banks)
            if self.last_state not in self.visited_states:
                self.cycles += 1
                self.visited_states[self.last_state] = self.cycles
            else:
                done = True


def part_a(input):
    memRealloc = MemoryReallocator(input)
    memRealloc.reallocate()
    return str(memRealloc.cycles + 1)


def part_b(input):
    memRealloc = MemoryReallocator(input)
    memRealloc.reallocate()
    return str(memRealloc.cycles + 1 - memRealloc.visited_states[memRealloc.last_state])


def solve(input):
    return {'a': part_a(input), 'b': part_b(input)}
