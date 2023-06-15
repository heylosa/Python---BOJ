#20920
import sys
N, M = map(int,input().split())


dic = {}
for _ in range (N):
    A = sys.stdin.readline().rstrip()
    if len(A) >= M:
        if A in dic:
            dic[A] += 1
        else:
            dic[A] = 1

dic = sorted(dic.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in dic:
    print(i[0])