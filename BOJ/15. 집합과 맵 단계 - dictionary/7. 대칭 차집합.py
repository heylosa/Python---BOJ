#1269번
#대칭 차집합의 구문은 (집합set1 ^ 집합set2) 로 구분된다.

N, M = map(int,input().split())

a = set(map(int,input().split()))
b = set(map(int,input().split()))

print(len(list(a ^ b)))