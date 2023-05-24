import sys

N = int(input())
list = []
for _ in range (N):
    A = int(sys.stdin.readline())
    list.append(A)

list.sort()

for i in list:
    print(i)