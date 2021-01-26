def solution(stones, k):
    answer = 0
    bridgelength = len(stones)
    flag = "start"

    while True:
        for i in range(bridgelength):
            if stones[i] != 0:
                stones[i] -=1
            else:
                for j in range(k):
                    if i+j+1 >= bridgelength:
                        break
                    if j == k-1:
                        flag = "end"
                        break
                    if stones[i+j+1] != 0:
                        stones[i+j+1] -=1
                        i=i+j+1
                        break
            if flag == "end":
                break
        if flag == "end":
            break
        answer += 1
    return answer