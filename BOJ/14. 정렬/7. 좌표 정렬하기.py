N = int(input())
Z = []
for i in range (N):
    x, y = map(int,input().split())
    Z.append([x,y])
Z.sort()
for i in range (N):
    print(*Z[i])

