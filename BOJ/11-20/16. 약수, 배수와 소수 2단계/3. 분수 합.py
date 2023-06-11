import math
A, B = map(int,input().split())
C, D = map(int,input().split())

z = A*D + B*C
w = B*D

m = math.gcd(z,w)
z //= m
w //= m
print(z, w)