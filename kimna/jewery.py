def solution(gems):
    answer = [0, 0]
    sub = []
    gemssub = []
    start, end = 0, 0
    gemslength, gemskind = len(gems), len(set(gems))
    kind = len(gemssub)

    while True:
        kind = len(set(gemssub))

        if kind == gemskind:
            sub.append((start, end))
            del gemssub[0]
            start += 1

        if end == gemslength:
            break

        if kind != gemskind:
            gemssub.append(gems[end])
            end += 1

    length = float('inf')
    for s, e in sub:
        if length > e - s:
            length = e - s
            answer[0] = s + 1
            answer[1] = e
    return answer