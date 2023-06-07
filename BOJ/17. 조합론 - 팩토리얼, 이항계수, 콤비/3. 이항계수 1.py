# 이항 계수는 N개의 물건 중 K개를 순서 없이 고르는 경우의 수 - 조합론에서 자주 나온다.
# https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients
# 이항계수 알고리즘 3가지에 대한 내용

import math
N, K = map(int,input().split())
print(math.comb(N, K))


def factorial(n):
    ans = 1
    for i in range (2, n+1):
        ans *= i
    return ans

# 팩토리얼을 사용한 이항계수의 정의

def bino_coef_factorial(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)


N, K = map(int,input().split())
print(bino_coef_factorial(N, K))