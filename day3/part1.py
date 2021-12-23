from typing import List

import numpy as np


def main(bits: List[str]):
    bits = np.array([[int(b) for b in bb.strip()] for bb in bits])
    med = np.median(bits, axis=0)
    gamma = int(''.join(str(int(m)) for m in med), base=2)
    epsilon = int(''.join(str(int(1-m)) for m in med), base=2)
    return gamma * epsilon


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))
