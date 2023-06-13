# 2108번
import sys; input = sys.stdin.readline
import statistics

lst = []
for _ in range (int(input().strip())):
    lst.append(int(input().strip()))


print(round(statistics.mean(lst)))
print(round(statistics.median(lst)))
print(round(statistics.mode(lst)))
print(round(max(lst)-min(lst)))