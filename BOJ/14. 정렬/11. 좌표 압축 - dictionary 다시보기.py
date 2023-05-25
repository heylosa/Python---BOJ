#1. 딕셔너리이름 = {"key값" : "value값"}
# 2. key 중복 허용 X
# 3. key가 중복 될 경우 마지막에 입력된 key의 value를 출력.
# ex)
# a = {"key1":"value1", "key2":"value2", "key1":"value3"
# print(a["key1"])
# 결과: value3
# 다시보기

import sys
N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
A = list(sorted(set(lst)))
B = {A[i]:i for i in range (len(A))}

for i in lst:
    print(B[i],end=' ')