from typing import List

import numpy as np


def part2(depths: List[int]):
    depths = np.array(depths)
    depths = depths[:-2] + depths[1:-1] + depths[2:]
    return (np.greater(depths[1:], depths[:-1])).sum()


if __name__ == '__main__':
    print(part2([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))
    print(part2([int(l) for l in open('input.txt').readlines()]))
