from itertools import permutations

import numpy as np


digit_codes = np.array([
    #A  B  C  D  E  F  G
    [1, 1, 1, 0, 1, 1, 1],  # 0
    [0, 0, 1, 0, 0, 1, 0],  # 1
    [1, 0, 1, 1, 1, 0, 1],  # 2
    [1, 0, 1, 1, 0, 1, 1],  # 3
    [0, 1, 1, 1, 0, 1, 0],  # 4
    [1, 1, 0, 1, 0, 1, 1],  # 5
    [1, 1, 0, 1, 1, 1, 1],  # 6
    [1, 0, 1, 0, 0, 1, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1],  # 9
], dtype=int)

digit_code_map = {tuple(code): i for i, code in enumerate(digit_codes)}


def unordered_hash(l):
    return sum(hash(i) for i in l)


all_mappings = np.array(list(permutations(range(7))))
permuted_digit_code_mappings = {unordered_hash(tuple(code) for code in digit_codes[:, mapping]): mapping for mapping in all_mappings}


def invert_permutation(permutation):
    inverted = np.zeros_like(permutation)
    inverted[permutation] = np.arange(permutation.shape[0])
    return inverted


def alpha_to_bin_array(alpha):
    bin_array = np.zeros(7, dtype=int)
    bin_array[list(ord(a) - ord('a') for a in alpha)] = 1
    return bin_array


def translate(observed_codes, target_codes):
    observed_codes = unordered_hash(tuple(alpha_to_bin_array(c)) for c in observed_codes.split())
    target_codes = np.array([alpha_to_bin_array(c) for c in target_codes.split()])

    mapping = permuted_digit_code_mappings[observed_codes]
    inv_mapping = invert_permutation(mapping)

    return [digit_code_map[tuple(c)] for c in target_codes[:, inv_mapping]]


def main(lines):
    translations = []
    for line in lines:
        all_codes, target_codes = line.strip().split(' | ')
        translations.append(int(''.join(str(d) for d in translate(all_codes, target_codes))))

    return sum(translations)


if __name__ == '__main__':
    print(main(open('input.txt').readlines()))
