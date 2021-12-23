from collections import defaultdict

import numpy as np


def is_large(node: str):
    return node.isupper()


def is_small(node: str):
    return node.islower() and node != 'start' and node != 'end'


def main(lines):
    links = np.array([line.strip().split('-') for line in lines])

    links_map = defaultdict(list)
    for a, b in links:
        links_map[a].append(b)
        links_map[b].append(a)

    frontier = {(None, 'start')}
    paths = []

    while len(frontier) > 0:
        path = frontier.pop()
        if path[-1] == 'end':
            paths.append(path)
            continue

        for next_ in links_map[path[-1]]:
            if is_large(next_) or next_ not in path:
                frontier.add(path + (next_,))
            elif is_small(next_) and path[0] is None:
                frontier.add((next_,) + path[1:] + (next_,))

    return len(paths)


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))
