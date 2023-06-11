import sys
T = int(sys.stdin.readline())
for i in range (T):
    R, S = map(str,sys.stdin.readline().split())
    for k in range (len(S)):
        print(S[k]*int(R), end='')
    print()