import re
from collections import namedtuple

Node = namedtuple('Node', 'base_weight total_weight children')


class Tree:
    def __init__(self):
        self.nodes = {}
        self.root = None

    def build(self, puzzle_input):
        for line in puzzle_input:
            m = re.search('([a-z]+) \((\d+)\)', line)
            if m is not None:
                name = m.group(1)
                weight = m.group(2)
                children = []
                parts = line.split(' -> ')
                if len(parts) > 1:
                    for child in parts[1].split(','):
                        children.append(child.strip())
                self.nodes[name] = Node(int(weight), 0, children)
        self._update_root()

    def find_unbalanced(self):
        self._update_total_weights()

        leaves = [k for k, v in self.nodes.items() if len(v.children) == 0]
        layer = set([self._get_parent(n) for n in leaves])

        unbalanced_state = None
        while not unbalanced_state:
            parents = set()
            for node in layer:
                parent = self._get_parent(node)
                parents.add(parent)
            for parent in parents:
                vals = {}
                for child in self.nodes[parent].children:
                    if self.nodes[child].total_weight not in vals:
                       vals[self.nodes[child].total_weight] = []
                    vals[self.nodes[child].total_weight].append(child)
                if len(vals) > 1:
                    unbalanced_state = vals
        # calc diff
        value, node = [(k, v) for k, v in unbalanced_state.items() if len(v) == 1][0]
        most_common_values = [k for k, v in unbalanced_state.items() if len(v) > 1][0]
        off = value - most_common_values

        return self.nodes[node[0]].base_weight - off

    def _update_root(self):
        all_childrens = set()
        potential_roots = set()
        for name, data in self.nodes.items():
            potential_roots.add(name)
            for child in data.children:
                all_childrens.add(child)
        potential_roots = potential_roots - all_childrens
        assert len(potential_roots) == 1
        self.root = potential_roots.pop()

    def _update_total_weights(self):
        root = self.nodes[self.root]
        self.nodes[self.root] = Node(
            root.base_weight,
            self._get_total_weight(self.root),
            root.children)

    def _get_total_weight(self, name):
        if len(self.nodes[name].children) == 0:
            return self.nodes[name].base_weight
        tot = self.nodes[name].base_weight
        for child in self.nodes[name].children:
            w = self._get_total_weight(child)
            self.nodes[child] = Node(self.nodes[child].base_weight, w, self.nodes[child].children)
            tot += w
        return tot

    def _get_parent(self, child):
        for k, v in self.nodes.items():
            if child in v.children:
                return k
        return ''
        

def part_a(puzzle_input):
    tree = Tree()
    tree.build(puzzle_input)

    return tree.root


def check(layer):
    parents = set()
    for l in layer:
        parent = get_parent(tree, l)
        parents.add(parent)
        vals = {}
        for c in tree[parent][1]:
            if tree[c][0] not in vals:
                vals[tree[c][0]] = []
            vals[tree[c][0]].append(c)
        if len(vals) > 1:
            print('PART2: ')
            print(vals)
    return parents

def part_b(puzzle_input):
    tree = Tree()
    tree.build(puzzle_input)
    unbalanced = tree.find_unbalanced()
    return str(unbalanced)


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
