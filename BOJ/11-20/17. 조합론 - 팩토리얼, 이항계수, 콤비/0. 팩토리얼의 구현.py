def factorial(n):
    ans = 1
    for i in range (2, n+1):
        ans *= i
    return ans

# 팩토리얼을 사용한 이항계수의 정의

def bino_coef_factorial(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)


#math의 combination을 사용하면 됨