# 브루트 포스
# 무차별 암호 대입 공격 / 무작위로 키를 계속 입력함으로써 해킹을 시도하는 공격 방식
# 2798번
# 세 장의 카드를 고르는 모든 경우를 고려하는 문제

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = []
for i in range (N):
    for j in range (i+1,N):
        for k in range (j+1,N):
            sum = A[i] + A[j] + A[k]
            if sum <= M:
                B.append(sum)

print(max(B))