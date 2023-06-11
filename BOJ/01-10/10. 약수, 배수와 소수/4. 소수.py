M = int(input())
N = int(input())

num = []
for i in range (M, N+1):
    error = 0
    if i > 1:
        for j in range (2, i):
            if i % j == 0:
                error += 1
                break
        if error == 0:
            num.append(i)

if len(num) > 0:
    print(sum(num))
    print(num[0])
else:
    print(-1)

