from collections import defaultdict
from copy import copy

import numpy as np


def unpack_bits(bits):
    return [(bits >> i) & 1 for i in range(4)]


def main(lines):
    bytes_ = np.array([unpack_bits(int(byte, 16)) for byte in lines[0].strip()]).flatten()



    return bytes_



if __name__ == '__main__':
    # print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))

