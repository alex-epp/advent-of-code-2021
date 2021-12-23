import numpy as np
from scipy.signal import correlate2d


def step(levels: np.ndarray):
    levels = levels + 1
    flashed = np.zeros_like(levels, dtype=bool)
    while True:
        new_flashers = (levels > 9) & ~flashed
        if new_flashers.sum() == 0: break
        flashed |= new_flashers
        energy_transfer = correlate2d(new_flashers, np.ones((3, 3)), mode='same')
        levels = levels + energy_transfer

    levels[flashed] = 0
    return flashed.sum(), levels


def main(lines, steps):
    levels = np.array([[int(digit) for digit in line.strip()] for line in lines])

    total_flashers = 0
    for _ in range(steps):
        flashers, levels = step(levels)
        total_flashers += flashers

    return total_flashers


if __name__ == '__main__':
    print(main(open('example.txt').readlines(), 10))
    print(main(open('example.txt').readlines(), 100))
    print(main(open('input.txt').readlines(), 100))

