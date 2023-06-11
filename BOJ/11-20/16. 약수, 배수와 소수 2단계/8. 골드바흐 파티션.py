# 17103 문제
# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.


# 시간초과 / 일반 소수 판별먹으로 소수 구한다음에 덧셈 O(N^2) 진행
# import sys
# T = int(input())
# for _ in range (T):
#     A = int(sys.stdin.readline())
#
#     num = []
#     for i in range (A):
#         error = 0
#         if i > 1:
#             for j in range (2, i):
#                 if i % j == 0:
#                     error += 1
#                     break
#             if error == 0:
#                 num.append(i)
#
#     cnt=0
#
#     for w in range (len(num)):
#         for k in range (w,len(num)):
#             if num[w]+num[k] != A:
#                 continue
#             else:
#                 cnt += 1
#     print(cnt)

# 시간초과 / 에라토스테네스의 체로 소수 구한다음에 전부 덧셈 진행
# import sys
#
# T = int(input())
# for _ in range (T):
#     n=int(sys.stdin.readline())
#     a = [False,False] + [True]*(n-1)
#     num=[]
#
#     for i in range(2,n+1):
#         if a[i]:
#             num.append(i)
#             for j in range(2*i, n+1, i):
#                 a[j] = False
#
#     cnt = 0
#     for w in range (len(num)):
#         for k in range (w,len(num)):
#             if num[w]+num[k] != n:
#                 continue
#             else:
#                 cnt += 1
#     print(cnt)



# 소수 미리 범위만큼 에라토스테네스체로 판별해서 리스트에 전부다 넣어놓음
# 주어진 N에서 소수를 빼서 소수면 count / 동시에 추가한 곳에 포함이 안되어 있으면 conut 세지 않음.


import sys

N = []
chk = [0] * 1000001
chk[0] = 1
chk[1] = 1

for i in range (2, 1000001):
    if chk[i] == 0:
        N.append(i)
        for j in range(2*i, 1000001, i): #마지막 증분을 나타내는 것, 간격을 나타내는 것 i의 배수는 i간격만큼을 의미)
            chk[j] = 1

T = int(input())

for _ in range (T):
    cnt = 0
    M = int(sys.stdin.readline())
    for i in N:
        if i >= M:
            break
        if not chk[M - i] and i <= M - i:
            cnt += 1
    print(cnt)