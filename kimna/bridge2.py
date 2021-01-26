def bridge(stones, k, mid):
    jump = k
    for i in stones:
        if i <= mid:
            jump -= 1
            if jump == 0:
                return False
        else:
            jump = k
    return True

def solution(stones, k):
    answer = 0
    left = 0
    right = 200000000

    while left < right:
        mid = (left+right) // 2
        if bridge(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid -1
    return answer+1