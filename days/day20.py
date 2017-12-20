"""--- Day 20: Particle Swarm ---"""
import re


class Particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def update(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

    def distance(self):
        return sum(abs(n) for n in self.p)

    def __repr__(self):
        return "p=<{0}>, v=<{1}>, a=<{2}>".format(self.p, self.v, self.a)


def closest_to_origin(puzzle_input, remove_collisions=False, iterations=350):
    particles = {}
    index = 0
    for line in puzzle_input:
        m = re.search('p=<(.+)>, v=<(.+)>, a=<(.+)>', line)
        if m is not None:
            particles[index] = Particle(
                [int(n) for n in m.group(1).strip().split(',')],
                [int(n) for n in m.group(2).strip().split(',')],
                [int(n) for n in m.group(3).strip().split(',')])
        index += 1
    for _ in range(iterations):
        for i, p in particles.items():
            p.update()
        if remove_collisions:
            positions = {}
            for i, p in particles.items():
                key = '|'.join(str(n) for n in p.p)
                if key not in positions:
                    positions[key] = []
                positions[key].append(i)
            for pos in positions:
                if len(positions[pos]) > 1:
                    for a in positions[pos]:
                        del particles[a]
    return particles


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    min_index = None
    min_distance = None
    for index, particle in closest_to_origin(puzzle_input).items():
        if min_distance is None or particle.distance() < min_distance:
            min_distance = particle.distance()
            min_index = index
    return str(min_index)


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    return str(len(closest_to_origin(puzzle_input, remove_collisions=True)))


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
