#1764번
import sys

N, M = map(int,input().split())
dic_1 = {}
dic_2 = {}

for i in range (N):
    dic_1[sys.stdin.readline().strip()] = i
for j in range (M):
    dic_2[sys.stdin.readline().strip()] = j

dic_1 = sorted(dic_1)
dic_2 = sorted(dic_2)

cnt = 0
for w in dic_1:
    if w in dic_2:
        cnt += 1

print(cnt)
for w in dic_1:
    if w in dic_2:
        print(w)
