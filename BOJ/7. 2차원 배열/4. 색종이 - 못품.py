# 일단 중복되는거 상관없이 리스트로 다 받고
# 중복되는 부분만 추출해서 넓이 구한다음에 300에서 빼는걸로 ㄱㄱ

import sys

arr = [[0 for _ in range(101)] for _ in range(101)] #2차원 배열 선언
N = int(sys.stdin.readline())

for _ in range(N):
    H, W = list(map(int,input().split()))

    for row in range (H,H+10):
        for col in range (W,W+10):
            arr[row][col] = 1

result = 0

for i in arr:
    result+= i.count(1)

print(result)
