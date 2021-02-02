def solution(s):
    answer = 0
    answer = len(s)
    kind = len(s) // 2 + 1
    wordlist = []

    for interval in range(kind, 0, -1):
        wordlist = [s[i:i + interval] for i in range(0, len(s), interval)]
        word = wordlist[0]
        num = 0
        result = ""
        for k in wordlist:
            if word == k:
                num += 1
            else:
                if num != 1:
                    result = result + str(num) + word
                else:
                    result = result + word
                word = k
                num = 1

        if num == 1:
            num = ""
        result = result + str(num) + word
        answer = min(answer, result)
    return answer