import sys

N = [sys.stdin.readline() for _ in range (5)]
arr_len = []

for i in range (5):
    arr_len.append(len(N[i]))

maximum = max(arr_len)

for j in range (15):
    for i in range (5):
        if len(N[i][j]) == 0:
            continue
        else:
            print(N[i][j], end='')

    print()

