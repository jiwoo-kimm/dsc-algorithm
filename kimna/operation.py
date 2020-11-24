import itertools


def calculate2(num1, num2, op):
    if op == '+':
        return str(int(num2) + int(num1))
    if op == '-':
        return str(int(num2) - int(num1))
    if op == '*':
        return str(int(num2) * int(num1))


def priority(op, operation):
    num = 0
    num = operation.index(op)
    return num


def calculate(expression, operation):
    stack = []
    temp_stack = []
    result_stack = []
    result = 0

    for i in expression:
        if i not in operation:
            stack.append(i)
        else:

            while len(temp_stack) != 0 and priority(i, operation) <= priority(temp_stack[-1], operation):
                stack.append(temp_stack.pop())

            temp_stack.append(i)

    while temp_stack:
        stack.append(temp_stack.pop())

    for i in stack:
        if i in operation:
            num1 = result_stack.pop()
            num2 = result_stack.pop()
            result_stack.append(calculate2(num1, num2, i))
        else:
            result_stack.append(i)
    result = result_stack.pop()

    return result


def solution(expression):
    answer = 0
    result = []
    number = []
    express = []
    op = []
    operation = ['+', '-', '*']
    index = 0

    for i in range(len(expression)):
        if expression[i] in operation:
            op.append(expression[i])
            theop = expression[i]
            thenum = expression[index:i]
            express.append(thenum)
            express.append(theop)
            index = i + 1

    express.append(expression[index:])

    opkind = len(set(op))
    op = set(op)
    op = list(itertools.permutations(op, opkind))

    for i in op:
        result.append(abs(int(calculate(express, i))))
    for k in result:
        if answer < k:
            answer = k
    return answer
