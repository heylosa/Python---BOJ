import sys
N = int(sys.stdin.readline())
number = str(input())
A = 0
for i in range(N):
    A += int(number[i])
print(A)

