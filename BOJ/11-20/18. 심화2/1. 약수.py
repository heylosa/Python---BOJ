N = int(input())
M = list(map(int,input().split()))
M.sort()

if N != 1:
    print(M[0]*M[N-1])
else:
    print(M[0]**2)d