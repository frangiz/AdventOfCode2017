"""--- Day 24: Electromagnetic Moat ---"""


class Moat:
    """An Electromagnetic Moat"""

    def __init__(self, puzzle_input):
        """ctor, nothing more exiting."""
        self.components = self.parse_components(puzzle_input)

    def build_bridges(self, start_port):
        """
        Build all valid bridges.

        Args:
            start_port (int): The starting port for the bridge.
        Returns:
            list: List of tuples with the components for the bridge.

        """
        res = []
        for b in Moat._generate_bridges([], start_port, self.components):
            res.append(b)
        return res

    def parse_components(self, puzzle_input):
        """
        Parse the components.

        Args:
            puzzle_input (list): Formatted as the provided input from the website.
        Returns:
            list: List of tuples of integers.

        """
        return [tuple(map(int, line.strip().split('/'))) for line in puzzle_input]

    @staticmethod
    def _generate_bridges(curr_bridge, port, components):
        """
        Generate bridges.

        A generator for creating the bridges. The search space might be
        big with a lot of invalid bridges, hence a custom method instead of
        using itertools.combinations(). It uses a subgenerator that was added
        to Python 3.3.

        """
        if not any(port in c for c in components):
            return None
        for connector in [c for c in components if port in c]:
            remaining_components = list(components)
            remaining_components.remove(connector)
            new_bridge = curr_bridge + [connector]
            yield new_bridge
            next_port = connector[1] if connector[0] == port else connector[0]
            # Syntax for Delegating to a Subgenerator
            # https://www.python.org/dev/peps/pep-0380/
            yield from Moat._generate_bridges(new_bridge, next_port, remaining_components)


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    moat = Moat(puzzle_input)
    max_strength = 0
    for bridge in moat.build_bridges(0):
        max_strength = max(max_strength, sum(sum(tup) for tup in bridge))
    return str(max_strength)


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    moat = Moat(puzzle_input)
    max_length = 0
    max_strength = 0
    for bridge in moat.build_bridges(0):
        if len(bridge) >= max_length:
            max_length = len(bridge)
            max_strength = max(max_strength, sum(sum(tup) for tup in bridge))
    return str(max_strength)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
