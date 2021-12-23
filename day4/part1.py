from typing import List

import numpy as np


def board_won(markers: np.ndarray):
    return np.max([
        markers.diagonal().mean(),
        markers.T.diagonal().mean(),
        markers.mean(axis=0).max(),
        markers.mean(axis=1).max(),
    ]) == 1


def board_score(number: int, board: np.ndarray, markers: np.ndarray):
    return board[markers == 0].sum() * number


def main(lines: List[str]):
    lines = [l.strip() for l in lines if len(l.strip())]

    inputs = [int(i) for i in lines.pop(0).split(',')]

    boards = [lines[i:i+5] for i in range(0, len(lines)-4, 5)]
    boards = [np.array([[int(n) for n in line.split()] for line in board]) for board in boards]
    markers = [np.zeros_like(board) for board in boards]

    for i in inputs:
        for b, m in zip(boards, markers):
            m[b == i] = 1
            if board_won(m):
                return board_score(i, b, m)


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))
