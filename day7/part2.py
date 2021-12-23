import numpy as np


def main(positions):
    max_cost = max(positions) - min(positions)
    costs = np.cumsum(np.arange(max_cost + 1))

    return min(
        sum(costs[abs(p - x)] for p in positions)
        for x in range(min(positions), max(positions)+1)
    )


if __name__ == '__main__':
    print(main([16,1,2,0,4,2,7,1,2,14]))
    print(main([int(i) for i in open('input.txt').readline().split(',')]))
