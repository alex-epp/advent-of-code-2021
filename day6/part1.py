import numpy as np


def main(fish, days):
    fish_by_lifetime = np.zeros(9, dtype=int)
    for f in fish:
        fish_by_lifetime[f] += 1

    for _ in range(days):
        fish_by_lifetime = np.roll(fish_by_lifetime, shift=-1)
        fish_by_lifetime[6] += fish_by_lifetime[8]

    return fish_by_lifetime.sum()


if __name__ == '__main__':
    print(main([3, 4, 3, 1, 2], 18))
    print(main([3, 4, 3, 1, 2], 80))
    print(main([int(i) for i in open('input.txt').readline().split(',')], 80))
