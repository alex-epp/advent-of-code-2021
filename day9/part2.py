from itertools import permutations

import numpy as np


def basin_flood_fill(x, y, augmented_heightmap, basin_indices, index):
    searched = set()
    to_search = {(x, y)}
    size = 0
    while len(to_search) > 0:
        x, y = to_search.pop()
        searched.add((x, y))
        if augmented_heightmap[x, y] == 9:
            continue

        basin_indices[x, y] = index
        size += 1

        if (x+1, y) not in searched and augmented_heightmap[x+1, y] != 9:
            to_search.add((x+1, y))
        if (x-1, y) not in searched and augmented_heightmap[x - 1, y] != 9:
            to_search.add((x - 1, y))
        if (x, y+1) not in searched and augmented_heightmap[x, y + 1] != 9:
            to_search.add((x, y + 1))
        if (x, y-1) not in searched and augmented_heightmap[x, y - 1] != 9:
            to_search.add((x, y - 1))

    return size


def main(lines):
    heightmap = np.array([[int(digit) for digit in line.strip()] for line in lines])

    augmented_heightmap = np.zeros((heightmap.shape[0] + 1, heightmap.shape[1] + 1))
    augmented_heightmap[:] = 9
    augmented_heightmap[:-1, :-1] = heightmap

    basin_indices = np.zeros_like(augmented_heightmap, dtype=int)
    basin_indices[:] = -1
    basin_sizes = []

    for x in range(heightmap.shape[0]):
        for y in range(heightmap.shape[1]):
            if heightmap[x, y] == 9: continue
            if basin_indices[x, y] >= 0: continue
            basin_sizes.append(basin_flood_fill(x, y, augmented_heightmap, basin_indices, len(basin_sizes)))

    a, b, c = np.array(sorted(basin_sizes, reverse=True))[:3]
    return a * b * c


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))

