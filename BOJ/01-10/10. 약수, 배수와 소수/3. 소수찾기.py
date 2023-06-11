T = int(input())
N = map(int,input().split())
sosu = 0
for i in N:
    much = 0
    if i > 1:
        for j in range (2,i):
            if i % j == 0:
                much += 1
        if much == 0:
            sosu += 1

print(sosu)