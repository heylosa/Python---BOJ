import sys
S = sys.stdin.readline().strip()
N = set()
for i in range(len(S)):
    for j in range(i,len(S)):
        N.add(S[i:j+1])

print(len(N))