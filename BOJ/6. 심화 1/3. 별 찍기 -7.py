import sys
N = int(sys.stdin.readline())
blank = ' '
star = '*'
for i in range (N):
    if i < N:
        print(blank*(N-i-1)+star*(2*i+1))

for i in range (N):
    print(blank*(i+1) + star*(2*N-3-2*i))