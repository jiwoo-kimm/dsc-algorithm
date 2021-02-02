import sys
sys.setrecursionlimit(10000000)

def find(number, room):
    if number not in room:
        room[number] = number + 1
        return number
    empty = find(room[number], room)
    room[number] = empty + 1
    return empty

def solution(k, room_number):
    answer = []
    room = dict()

    for number in room_number:
        emptyroom = find(number, room)
        answer.append(emptyroom)

    return answer