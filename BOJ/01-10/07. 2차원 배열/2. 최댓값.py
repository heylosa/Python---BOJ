import sys

arr = [list(map(int,sys.stdin.readline().split())) for _ in range (9)]
arr_max = []

for i in range (9):
    arr_max.append(max(arr[i]))

arr_max_index = arr_max.index(max(arr_max))

print(max(arr_max))
print(arr_max_index+1, arr[arr_max_index].index(max(arr[arr_max_index]))+1)