import sys
import math

T = int(input())
for i in range (T):
    A, B = map(int,sys.stdin.readline().strip().split())
    print(A*B//math.gcd(A,B))


    # if A < B:
    #     for j in range (1, B):
    #         if A % j == 0 and B % j == 0:
    #             gcd = j
    # else:
    #     for w in range (1, A):
    #         if A % w == 0 and B % w == 0:
    #             gcd = w
    # print(A * B // gcd)