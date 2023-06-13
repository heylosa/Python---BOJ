# 10828번
# 스택의 개념을 익히고 실습하는 문제
# 파이썬은 따로 stack 구조를 제공하지 않는다.
# 기본 클래스 list를 이용하여 stack을 표현해야 한다.
# pop같은 경우는 내장함수로 존재, 마지막 인수를 제거후 출력 / 정수가 없는 경우는 -1출력하도록 써줘야함

import sys
N = int(input())

stack = []
for _ in range (N):
    A = sys.stdin.readline().split()
    if A[0] == 'push':
        stack.append(A[1])
    elif A[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif A[0] == 'size':
        print(len(stack))
    elif A[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif A[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])