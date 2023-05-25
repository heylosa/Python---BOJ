import sys
N = int(input())
A = []

for i in range (N):
    A.append(sys.stdin.readline().strip())
A_set = set(A)
A = list(A_set)
A.sort()
A.sort(key = len)

for i in A:
    print(i)

