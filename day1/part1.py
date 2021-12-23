from typing import List

import numpy as np


def part1(depths: List[int]):
    return(np.greater(depths[1:], depths[:-1])).sum()


if __name__ == '__main__':
    print(part1([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))
    print(part1([int(l) for l in open('input.txt').readlines()]))
