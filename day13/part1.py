from collections import defaultdict

import numpy as np


def main(lines):
    dots = np.array([[int(n) for n in line.strip().split(',')] for line in lines if line != '\n' and not line.startswith('fold')], dtype=int)
    fold_strings = [line.strip() for line in lines if line.startswith('fold')]

    folds = []
    for fold in fold_strings:
        if fold.startswith('fold along x='):
            folds.append((0, int(fold[13:])))
        else:
            folds.append((1, int(fold[13:])))

    for axis, amount in folds:
        dots[:, axis] = amount - np.abs(dots[:, axis] - amount)

    extent = dots.max(axis=0) + 1
    dots = set(tuple(dot) for dot in dots)
    for y in range(extent[1]):
        for x in range(extent[0]):
            if (x, y) in dots: print('#', end='')
            else: print('.', end='')
        print()

    return len(dots)


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))

