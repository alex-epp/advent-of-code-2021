from collections import defaultdict
from copy import copy


def main(lines):
    lines = [l.strip() for l in lines if len(l.strip()) > 0]
    initial_state = lines.pop(0)

    pairs = defaultdict(int)
    for i in range(len(initial_state)-1):
        pairs[initial_state[i] + initial_state[i+1]] += 1

    for _ in range(10):
        # print(pairs)
        new_pairs = defaultdict(int)
        for line in lines:
            pair, inserted = line.split(' -> ')
            if not pair in pairs: continue
            n = pairs.pop(pair)
            new_pairs[pair[0] + inserted] += n
            new_pairs[inserted + pair[1]] += n

        for k, v in new_pairs.items():
            pairs[k] += v

    counts = defaultdict(int)
    for pair, count in pairs.items():
        counts[pair[0]] += count / 2
        counts[pair[1]] += count / 2
    counts[initial_state[0]] += 0.5
    counts[initial_state[-1]] += 0.5

    return max(counts.values()) - min(counts.values())


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))

