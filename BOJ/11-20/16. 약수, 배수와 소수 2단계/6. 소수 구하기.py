# 에라토스테네스의 체를 이용한 소수 구하기
#
# n=1000
# a = [False,False] + [True]*(n-1)
# primes=[]
#
# for i in range(2,n+1):
#   if a[i]:
#     primes.append(i)
#     for j in range(2*i, n+1, i):
#         a[j] = False
# print(primes)
#


a, b = map(int,input().split())
n = b
K = [False,False] + [True]*(n-1)
primes=[]
for i in range (2, b+1):
    if K[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            K[j] = False

for w in range (len(primes)):
    if primes[w] >= a:
        print(primes[w])


