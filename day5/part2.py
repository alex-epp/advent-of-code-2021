from typing import List

import numpy as np


def main(lines: List[str]):
    lines = np.array([[[int(p) for p in point.split(',')] for point in line.strip().split(' -> ')] for line in lines])

    extent = lines.max(axis=(0, 1)) + 1
    map = np.zeros(extent)

    for ((x1, y1), (x2, y2)) in lines:
        x, y = x1, y1
        x_step, y_step = np.sign(x2 - x1), np.sign(y2 - y1)
        x_end = x2 + x_step
        y_end = y2 + y_step
        while x != x_end or y != y_end:
            map[x, y] += 1
            x += x_step
            y += y_step

    return (map > 1).sum()


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))
