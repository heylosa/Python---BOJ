#1764번
#집합 자료형의 활용 문제
#기존에는 dictionary를 활용한 O(1) 시간 복잡도로 단순활용을 진행했지만, for을 이중으로 사용함으로써 더 오래 시간이 걸리게 된다.
#두 집합에서 교집합/차집합 부분을 구할때는 a/b 리스트를 set() 을 통해 집합화 시키고, add()를 통해서 입력값을 집합에 추가시킨다.
#이후 결과 값에 a & b를 이용해 교집합을 구해주는 문제

import sys

N, M = map(int,input().split())
a = set()
b = set()

for i in range (N):
    a.add(sys.stdin.readline().strip())
for j in range (M):
    b.add(sys.stdin.readline().strip())

result = sorted(list(a & b))

print(len(result))
for i in result:
    print(i)