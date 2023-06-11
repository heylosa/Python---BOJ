import sys

while True:
    a= int(sys.stdin.readline())
    if a != 0:
        n = 2*a
        K = [False,False] + [True]*(n-1)
        primes=[]
        for i in range (2, 2*a+1):
            if K[i]:
                primes.append(i)
                for j in range(2*i, n+1, i):
                    K[j] = False

        zero = 0
        for w in range (len(primes)):
            if primes[w] > a:
                zero += 1
        print(zero)
    else:
        break

#다른사람 풀이 / 루트로 소수를 체크하는 풀이인듯?
#루트로 소수를 전부다 체크해놓는다.
#이후에 검색한 값을 돌려서 검색한 값의 카운트를 더한다.

num = 123456 * 2 + 1
num_list = [1] * num

for i in range(1, num):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            num_list[i] = 0
            break

while True:
    n = int(input())

    if n == 0:
        break

    prime = 0
    for i in range(n + 1, 2 * n + 1):
        prime += num_list[i]
    print(prime)