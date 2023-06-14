# 2108번
import sys; input = sys.stdin.readline
import statistics

lst = []
for _ in range (int(input().rstrip())):
    lst.append(int(input().rstrip()))


print(round(statistics.mean(lst)))
print(statistics.median(lst))

dic={}
for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 0

maximum = max(dic.values())
max_lst = []

for i in dic:
    if maximum == dic[i]:
        max_lst.append(i)

max_lst.sort()

if len(max_lst) > 1:
    print(max_lst[1])
else:
    print(max_lst[0])


print(max(lst)-min(lst))