#2292번

N = int(input())

def S(n):
    if n == 1:
        return 1
    else:
        return 3*n*(n-1)+1

n = 1

while True:
    if S(n) >= N:
        print(n)
        break
    else:
        n = n+1



######## or

N = int(input())

def S(n):
    if n == 1:
        return 1
    else:
        return 3*n*(n-1)+1

n = 1

while S(n) < N:
    n += 1

print(n)