# 에라토스테네스의 체를 이용한 소수 구하기
# 소수의 배수들을 지우면서 소수를 남기는 방법 / 리스트 2개를 만들어서 check 하면서 또 다른 소수 리스트에 소수를 넣는 것.

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

# 이게 좀 더 직관적이다.
prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1


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


