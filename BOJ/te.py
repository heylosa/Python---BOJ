N = int(input())
A = set(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))

for num in lst:
    print(1) if num in A else print(0)