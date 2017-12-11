def dist_flat_top_hex_grid(path):
    """https://www.redblobgames.com/grids/hexagons/#coordinates ."""
    x = 0
    y = 0
    z = 0
    max_distance = 0
    for direction in path.split(','):
        if direction == 'n':
            y += 1
            z += -1
        elif direction == 'ne':
            x += 1
            z += -1
        elif direction == 'se':
            x += 1
            y += -1
        elif direction == 's':
            y += -1
            z += 1
        elif direction == 'sw':
            x += -1
            z += 1
        elif direction == 'nw':
            x += -1
            y += 1
        else:
            raise ValueError('Invalid direction: {0}'.format(direction))
        max_distance = max(max_distance, (abs(x) + abs(y) + abs(z)) // 2)
    # Manhattan distance for a hex grid is the Manhattan distance
    # divided by 2.
    # https://www.redblobgames.com/grids/hexagons/#distances
    return ((abs(x) + abs(y) + abs(z)) // 2, max_distance)


def part_a(puzzle_input):
    return str(dist_flat_top_hex_grid(''.join(puzzle_input).strip())[0])


def part_b(puzzle_input):
    return str(dist_flat_top_hex_grid(''.join(puzzle_input).strip())[1])


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
