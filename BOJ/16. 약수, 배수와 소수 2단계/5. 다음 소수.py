import sys
T = int(input())

for i in range (T):
    A = int(sys.stdin.readline())
    B = 0
    err = 0
    while True:
        B = A
        B += 1
        if A % B == 0:
            print(A)
            err += 1
            break

