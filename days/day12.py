from collections import deque


def get_graph(puzzle_input):
    graph = {}
    for line in puzzle_input:
        key, neighbours = line.split('<->')
        graph[int(key)] = [int(i) for i in neighbours.split(',')]
    return graph


def find_group(program_id, graph):
    visited = set()
    unvisited = deque()
    unvisited.append(program_id)
    while unvisited:
        program = unvisited.pop()
        visited.add(program)
        for neighbour in graph[program]:
            if neighbour not in visited:
                unvisited.append(neighbour)
    return visited


def find_all_groups(graph):
    all_programs = graph.keys()
    groups = []
    for program in all_programs:
        group = sorted(list(find_group(program, graph)))
        if group not in groups:
            groups.append(group)
    return groups


def part_a(puzzle_input):
    graph = get_graph(puzzle_input)
    return str(len(find_group(0, graph)))


def part_b(puzzle_input):
    graph = get_graph(puzzle_input)
    return str(len(find_all_groups(graph)))


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
