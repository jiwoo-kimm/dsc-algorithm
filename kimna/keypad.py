def handlength(hand, number):
    number = str(number)
    location_x = {'1': 0, '2': 0, '3': 0,
                  '4': 1, '5': 1, '6': 1,
                  '7': 2, '8': 2, '9': 2,
                  '*': 3, '0': 3, '#': 3}

    location_y = {'1': 0, '2': 1, '3': 2,
                  '4': 0, '5': 1, '6': 2,
                  '7': 0, '8': 1, '9': 2,
                  '*': 0, '0': 1, '#': 2}
    hand_x = location_x[hand]
    hand_y = location_y[hand]
    number_x = location_x[number]
    number_y = location_y[number]
    result = abs(hand_x - number_x) + abs(hand_y - number_y)
    return result


def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = str(number)
        elif number in [3, 6, 9]:
            answer += 'R'
            right = str(number)
        else:
            lefthand = handlength(left, number)
            righthand = handlength(right, number)

            if lefthand < righthand:
                answer += 'L'
                left = str(number)
            elif lefthand > righthand:
                answer += 'R'
                right = str(number)
            else:
                if (hand == 'right'):
                    answer += 'R'
                    right = str(number)
                else:
                    answer += 'L'
                    left = str(number)
    return answer