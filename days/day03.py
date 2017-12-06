from util import Point, get_adjecent


class Grid:
    def __init__(self):
        self.values = {}
        self.pos = Point(0, 0)

    def gen_cells(self, cell_value_func, stop_func):
        self.values[Point(0, 0)] = 1
        for _ in range(10000000):  # just a big number
            if stop_func(self.pos):
                break
            self.take_step()
            self.add_cell_to_values(cell_value_func)

    def take_step(self):
        right = Point(self.pos.x + 1, self.pos.y)
        top = Point(self.pos.x, self.pos.y - 1)
        left = Point(self.pos.x - 1, self.pos.y)
        bottom = Point(self.pos.x, self.pos.y + 1)

        if self.has_none([top, left, bottom, right]):
            self.pos = Point(self.pos.x + 1, self.pos.y)
        elif self.has_all([left]) and self.has_none([top, right]):
            self.pos = Point(self.pos.x, self.pos.y - 1)
        elif self.has_all([bottom]) and self.has_none([left, top]):
            self.pos = Point(self.pos.x - 1, self.pos.y)
        elif self.has_all([right]) and self.has_none([left, bottom]):
            self.pos = Point(self.pos.x, self.pos.y + 1)
        elif self.has_all([top]) and self.has_none([right, bottom]):
            self.pos = Point(self.pos.x + 1, self.pos.y)
        else:
            raise Exception('Logic error?')

    def add_cell_to_values(self, cell_value_func):
        if self.pos not in self.values:
            self.values[self.pos] = cell_value_func(self.pos)

    def has_all(self, positions):
        return all(p in self.values for p in positions)

    def has_none(self, positions):
        return not any(p in self.values for p in positions)


def part_a(puzzle_input):
    target = int(''.join(puzzle_input))
    grid = Grid()
    grid.gen_cells(
        lambda pos: len(grid.values) + 1,
        lambda pos: grid.values[pos] == target)
    return str(abs(grid.pos.x) + abs(grid.pos.y))


def part_b(puzzle_input):
    target = int(''.join(puzzle_input))
    grid = Grid()
    grid.gen_cells(
        lambda pos: sum(grid.values[a] for a in get_adjecent(pos) if a in grid.values),
        lambda pos: grid.values[pos] > target)
    return str(grid.values[grid.pos])


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
