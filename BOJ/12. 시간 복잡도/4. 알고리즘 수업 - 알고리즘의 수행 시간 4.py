# 24265번
# MenOfPassion(A[], n)
#     sum = 0
#     for i in range (1, n-1)
#         for j in range (i+1, n)
#             sum = sum + A[i] * A[j]
# n-2번

n = int(input())
print(int(1/2 * n * (n -1)))
print(2)