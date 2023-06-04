#다시보기

import math
import sys
from math import gcd
N = int(input())
a = int(input())
A = []
for i in range (N-1):
    number = int(sys.stdin.readline())
    A.append(number-a)
    a = number

gcd = A[0]
for j in range (1, len(A)):
    gcd = math.gcd(gcd,A[j])

R = 0
for w in A:
    R += w // gcd - 1

print(R)