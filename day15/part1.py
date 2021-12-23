from collections import defaultdict
from copy import copy

import numpy as np


def main(lines):
    lines = [l.strip() for l in lines if len(l.strip()) > 0]
    grid = np.array([[int(l) for l in line] for line in lines])

    frontier = {(0, 0): (0, [(0, 0)])}
    visited = {}
    end = (grid.shape[0] - 1, grid.shape[1] - 1)

    while len(frontier):
        x, y = min(frontier.keys(), key=lambda k: frontier[k][0])
        cost, path = frontier.pop((x, y))
        visited[(x, y)] = cost, path

        if (x, y) == end:
            return cost

        neighbours = []
        if x > 0: neighbours.append((x - 1, y))
        if x < grid.shape[0] - 1: neighbours.append((x + 1, y))
        if y > 0: neighbours.append((x, y - 1))
        if y < grid.shape[1] - 1: neighbours.append((x, y + 1))

        for nx, ny in neighbours:
            if (nx, ny) in visited: continue
            if (nx, ny) in frontier and frontier[(nx, ny)][0] <= cost + grid[(nx, ny)]: continue
            frontier[(nx, ny)] = cost + grid[(nx, ny)], path + [(nx, ny)]

    raise ValueError()


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))

