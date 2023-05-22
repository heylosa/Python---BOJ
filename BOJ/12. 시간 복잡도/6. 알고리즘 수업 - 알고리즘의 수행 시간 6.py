#24267번
# def MenOfPassion (A[], n):
#     sum = 0
#     for i in range (1, n-2)
#         for j in range (i+1, n-1)
#             for k in range (j+1, n)
#                 sum = sum + A[i] × A[j] × A[k] # 코드1

#전체 n-2

n = int(input())
sum = 0
num = n-2
for i in range (1, n-1):
    sum += (num * i)
    num -= 1

print(sum)
print(3)
