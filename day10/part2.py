chunk_openings = ['(', '[', '{', '<']
chunk_closings = [')', ']', '}', '>']
error_scores = [3, 57, 1197, 25137]
autocomplete_scores = [1, 2, 3, 4]

chunk_closings_map = {c: o for o, c in zip(chunk_openings, chunk_closings)}
error_scores_map = {c: s for c, s in zip(chunk_closings, error_scores)}
autocomplete_scores_map = {o: s for o, s in zip(chunk_openings, autocomplete_scores)}


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


def autocomplete_score(line: str):
    stack = []
    for c in line:
        if c in chunk_openings:
            stack.append(c)
        elif c in chunk_closings:
            if len(stack) == 0 or chunk_closings_map[c] != stack[-1]:
                raise ValueError()
            stack.pop()
        else:
            raise ValueError()

    score = 0
    for c in reversed(stack):
        score = score * 5 + autocomplete_scores_map[c]
    return score


def main(lines):
    incomplete_lines = [l for l in lines if syntax_error_score(l.strip()) == 0]
    scores = sorted(autocomplete_score(l.strip()) for l in incomplete_lines)
    return scores[len(scores)//2]


if __name__ == '__main__':
    print(main(open('example.txt').readlines()))
    print(main(open('input.txt').readlines()))

