import functools


class KnotHash():
    def __init__(self, num_registers):
        self.registers = [i for i in range(num_registers)]
        self.index = 0
        self.skip = 0

    def calc_hash(self, lengths):
        ascii_tokens = [ord(c) for c in lengths]
        ascii_tokens += [17, 31, 73, 47, 23]
        for _ in range(64):
            self.knot_hash(ascii_tokens)
        sparse_hash = self.registers
        dense_hash = []
        for block in [sparse_hash[i:i + 16] for i in range(0, len(sparse_hash), 16)]:
            dense_hash.append(functools.reduce(lambda x, y: x ^ y, block, 0))
        return ''.join('{:02x}'.format(dh) for dh in dense_hash)

    def knot_hash(self, lengths):
        len_registers = len(self.registers)
        for length in lengths:
            if length > len_registers:
                continue
            # collect items
            items = self.registers[self.index:length + self.index]
            if len(items) < length:
                items += self.registers[0:length - len(items)]
            # reverse them
            items.reverse()
            for i in range(len(items)):
                self.registers[(i + self.index) % len_registers] = items[i]
            self.index = (self.index + length + self.skip) % len_registers
            self.skip += 1


def part_a(puzzle_input):
    kh = KnotHash(256)
    kh.knot_hash(list(map(int, ''.join(puzzle_input).split(','))))
    return str(kh.registers[0] * kh.registers[1])


def part_b(puzzle_input):
    kh = KnotHash(256)
    return kh.calc_hash(''.join(puzzle_input).strip())


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
