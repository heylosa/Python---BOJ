# 2231번
# 모든 경우를 시도하여 N의 생성자를 구하는 문제

N = int(input())
for i in range (1,N+1):
    n = sum((map(int,str(i))))
    n_sum = i + n
    if n_sum == N:
        print(i)
        break
    if i == N:
        print(0)