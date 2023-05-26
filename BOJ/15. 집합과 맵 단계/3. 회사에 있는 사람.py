import sys
n = int(input())
name_lst = {}
for i in range (n):
    a,b = map(str,sys.stdin.readline().split())

    if b == "enter":
        name_lst[a] = b
    else:
        del name_lst[a]

name_lst = sorted(name_lst, reverse= True)

for j in name_lst:
    print(j)