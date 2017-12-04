from itertools import permutations


def part_a(input):
    res = 0
    for line in input:
        words = line.split()
        if len(words) == len(set(words)):
            res += 1
    return str(res)


def part_b(input):
    res = 0
    for line in input:
        words = line.split()
        valid = True
        for word in words:
            other_words = [w for w in words if w != word]
            # check if we removed more than one copy of the word
            if (len(other_words) + 1 != len(words)):
                valid = False
            else:
                if any(''.join(p) in other_words for p in permutations(word)):
                    valid = False
        res += 1 if valid else 0
    return str(res)


def solve(input):
    return {'a': part_a(input), 'b': part_b(input)}
