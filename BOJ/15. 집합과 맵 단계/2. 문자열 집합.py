import sys
N, M = map(int,input().split())
S = []
check = []
for i in range (N):
    S.append(sys.stdin.readline())
for j in range (M):
    check.append(sys.stdin.readline())

S_dic = {}
for w in range (N):
    S_dic[S[w]] = 0

cnt = 0
for m in range (M):
    if check[m] in S_dic:
       cnt += 1

print(cnt)