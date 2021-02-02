from itertools import permutations


def search(user_set, banned_set):
    userlength = len(user_set)
    for k in range(userlength):
        wordlength = len(user_set[k])
        banlength = len(banned_set[k])
        if wordlength != banlength:
            return False
        for j in range(wordlength):
            if banned_set[k][j] == '*':
                continue
            if user_set[k][j] != banned_set[k][j]:
                return False
    return True


def solution(user_id, banned_id):
    answerlist = []
    answer = 0

    for candidate in permutations(user_id, len(banned_id)):
        if search(candidate, banned_id):
            candidate = set(candidate)
            if candidate not in answerlist:
                answerlist.append(candidate)

    answer = len(answerlist)
    return answer