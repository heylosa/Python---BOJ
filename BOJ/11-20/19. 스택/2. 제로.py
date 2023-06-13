# 10773번
# 가장 최근에 쓴 수를 지우는 문제

import sys

K = int(input())
stack = []
for _ in range (K):
    A = int(sys.stdin.readline().rstrip())
    if A == 0:
        stack.pop()
    else:
        stack.append(A)

print(sum(stack))

