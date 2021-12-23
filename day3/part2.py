from typing import List

import numpy as np


def o2_generator_rating(bits: np.ndarray):
    for i_col in range(bits.shape[1]):
        f = bits[:, i_col] == 1
        if f.sum() >= (~f).sum():
            bits = bits[f]
        else:
            bits = bits[~f]
        if bits.shape[0] == 1:
            return int(''.join(str(b) for b in bits[0]), base=2)
    raise ValueError()


def co2_scrubber_rating(bits: np.ndarray):
    for i_col in range(bits.shape[1]):
        f = bits[:, i_col] == 1
        if f.sum() < (~f).sum():
            bits = bits[f]
        else:
            bits = bits[~f]
        if bits.shape[0] == 1:
            return int(''.join(str(b) for b in bits[0]), base=2)
    raise ValueError()


def main(bits: List[str]):
    bits = np.array([[int(b) for b in bb.strip()] for bb in bits])
    o2 = o2_generator_rating(bits)
    co2 = co2_scrubber_rating(bits)
    return o2 * co2


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))
