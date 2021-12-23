from typing import List

import numpy as np


def main(lines: List[str]):
    lines = np.array([[[int(p) for p in point.split(',')] for point in line.strip().split(' -> ')] for line in lines])

    extent = lines.max(axis=(0, 1)) + 1
    map = np.zeros(extent)

    for ((x1, y1), (x2, y2)) in lines:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        if x1 == x2 or y1 == y2:
            map[x1:x2+1][:, y1:y2+1] += 1

    return (map > 1).sum()


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))
