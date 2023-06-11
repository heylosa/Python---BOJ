#lambda 숙지 해야할 필요 있음
N = int(input())
Z = []
for i in range (N):
    x, y = map(int,input().split())
    Z.append([x,y])
Z.sort(key=lambda x: (x[1], x[0]))
for i in range (N):
    print(*Z[i])

