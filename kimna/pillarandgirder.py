def check(answer):
    for x, y , thing in answer:
        if thing == 0: #기둥
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        elif thing == 1: #보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
        else:
            return False
    return True


def solution(n, build_frame):
    answer = [[]]
    number = len(build_frame)

    for x, y , thing, build in range(number):
        if build == 1: #설치
            answer.append([x,y,thing])
            if check(answer) is False:
                answer.remove([x, y, thing])
        else:
            answer.remove([x, y, thing])
            if check(answer) is False:
                answer.append([x, y, thing])
    answer.sort()
    return answer