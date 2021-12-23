import numpy as np


def main(positions):
    return min(
        np.abs((np.array(positions) - x)).sum()
        for x in range(min(positions), max(positions)+1)
    )


if __name__ == '__main__':
    print(main([16,1,2,0,4,2,7,1,2,14]))
    print(main([int(i) for i in open('input.txt').readline().split(',')]))
