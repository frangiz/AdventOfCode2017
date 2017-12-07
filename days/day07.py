from collections import Counter, deque
from treelib import Tree
import re


def build_tree(puzzle_input):
    # parse input into links
    links = {}
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
            links[name] = (int(weight), children)
    # find the root
    potential_roots = set(links.keys())
    for k, v in links.items():
        for child in v[1]:
            potential_roots.discard(child)
    assert len(potential_roots) == 1
    root = potential_roots.pop()

    # build the tree
    tree = Tree()
    tree.create_node(root, root, data=links[root][0])
    children = [(root, c) for c in links[root][1]]
    while children:
        parent, node = children.pop()
        tree.create_node(node, node, parent=parent, data=links[node][0])
        for child in links[node][1]:
            children.append((node, child))
    return tree


def calc_new_weight_for_unbalanced_node(tree):
    leaves = [n for n in tree.all_nodes() if n.is_leaf()]
    total_weights = {n.tag: n.data for n in leaves}
    unvisited = deque(set(tree.parent(n.tag).tag for n in leaves))
    while unvisited:
        tag = unvisited.popleft()
        children = tree.children(tag)
        # check if we have visited all children
        if not all(child.tag in total_weights for child in children):
            unvisited.append(tag)
            continue
        # check if done
        child_weights = [total_weights[c.tag] for c in children]
        # true if we found the parent for the unbalanced node
        if len(set(child_weights)) > 1:
            c = Counter(child_weights)
            least_common = c.most_common()[-1][0]
            most_common = c.most_common()[0][0]
            for c in children:
                if total_weights[c.tag] == least_common:
                    return c.data + most_common - least_common

        # nope, carry on...
        total_weight = tree.get_node(tag).data
        total_weight += sum(total_weights[c.tag] for c in children)
        total_weights[tag] = total_weight
        parent_tag = tree.parent(tag).tag
        if parent_tag is not None and parent_tag not in unvisited:
            unvisited.append(parent_tag)
    return 0


def part_a(puzzle_input):
    tree = build_tree(puzzle_input)
    return tree.root


def part_b(puzzle_input):
    tree = build_tree(puzzle_input)
    return str(calc_new_weight_for_unbalanced_node(tree))


def solve(puzzle_input):
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
