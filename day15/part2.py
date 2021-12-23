import heapq
from collections import defaultdict
from copy import copy
from dataclasses import dataclass, field

import numpy as np


def main(lines):
    lines = [l.strip() for l in lines if len(l.strip()) > 0]
    grid = np.array([[int(l) for l in line] for line in lines])

    w, h = grid.shape
    grid = np.tile(grid, (5, 5))
    for x in range(5):
        for y in range(5):
            grid[w*x:w*(x+1), h*y:h*(y+1)] += x + y

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            while grid[i, j] > 9:
                grid[i, j] -= 9

    frontier = [(0, (0, 0))]
    costs = {(0, 0): 0}
    visited = {}
    end = (grid.shape[0] - 1, grid.shape[1] - 1)

    while len(frontier):
        cost, (x, y) = heapq.heappop(frontier)
        visited[(x, y)] = cost

        if (x, y) == end:
            return cost

        neighbours = []
        if x > 0: neighbours.append((x - 1, y))
        if x < grid.shape[0] - 1: neighbours.append((x + 1, y))
        if y > 0: neighbours.append((x, y - 1))
        if y < grid.shape[1] - 1: neighbours.append((x, y + 1))

        for nx, ny in neighbours:
            if (nx, ny) in visited: continue
            ncost = cost + grid[(nx, ny)]
            if (nx, ny) in costs and costs[(nx, ny)] <= ncost: continue
            heapq.heappush(frontier, (ncost, (nx, ny)))
            costs[(nx, ny)] = ncost

    raise ValueError()


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))

