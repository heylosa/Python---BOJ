import sys
C = int(sys.stdin.readline())

for _ in range (C):
    all = list(map(float,input().split()))
    average = sum(all[1:]) / all[0]
    above_average = len([b for b in all[1:] if b > average])
    percent = above_average / all[0] * 100
    print(f"{percent:.3f}%")


import sys
T = int(input())
