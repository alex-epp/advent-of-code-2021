import numpy as np


chunk_openings = ['(', '[', '{', '<']
chunk_closings = [')', ']', '}', '>']
error_scores = [3, 57, 1197, 25137]

chunk_closings_map = {c: o for o, c in zip(chunk_openings, chunk_closings)}
error_scores_map = {c: e for c, e in zip(chunk_closings, error_scores)}

def syntax_error_score(line: str):
    stack = []
    for c in line:
        if c in chunk_openings:
            stack.append(c)
        elif c in chunk_closings:
            if len(stack) == 0 or chunk_closings_map[c] != stack[-1]:
                return error_scores_map[c]
            stack.pop()
        else:
            raise ValueError()
    return 0


def main(lines):
    return sum(syntax_error_score(line.strip()) for line in lines)


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))

