# 값이 같은 원소의 전후관계가 바뀌지 않는 정렬 알고리즘을 안정 정렬(stable sort)이라고 합니다.

N = int(input())
Z = []
for i in range (N):
    x, y = map(str,input().split())
    x = int(x)
    Z.append([x,y])
Z.sort(key =lambda x: (x[0]))
for i in Z:
    print(i[0], i[1])



import sys

N = int(input())
Z = []
for i in range (N):
    x, y = sys.stdin.readline().rstrip().split()
#x에 대한 인트선언이 필요하다. 배열에 대한 정렬이라 그런가 ,,?
    x = int(x)
    Z.append([x,y])
Z.sort(key =lambda x: (x[0]))
for i in Z:
    print(i[0], i[1])