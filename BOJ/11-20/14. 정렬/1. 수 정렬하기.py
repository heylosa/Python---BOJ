N = int(input())
list = []
for _ in range (N):
    A = int(input())
    list.append(A)

list.sort()

for i in range (len(list)):
    print(list[i])