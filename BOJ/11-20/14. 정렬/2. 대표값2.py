list = []
for i in range (5):
    A = int(input())
    list.append(A)
list.sort()
print(int(sum(list)/5))
print(list[2])
