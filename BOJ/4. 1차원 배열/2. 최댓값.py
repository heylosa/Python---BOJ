group = []
for i in range(9):
    num = int(input())
    group.append(num)

maxn = max(group)
indexn = group.index(maxn)
print(maxn,indexn+1)