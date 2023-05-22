import sys

N, M = map(int,sys.stdin.readline().split())

matrix_N = [list(map(int,input().split())) for _ in range (N)]
matrix_M = [list(map(int,input().split())) for _ in range (M)]

for i in range (N):
    for j in range (M):
        print(matrix_N[i][j] + matrix_M[i][j], end=' ')
    print()
