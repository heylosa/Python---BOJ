import sys
N = int(input())

N2 = 0
for _ in range(N):
    A, B = sys.stdin.readline().rstrip().split()
    N2 += 1
    if A or B == 'ChongChong':
        break

dia=set()
for _ in range(N-N2):
    A, B = sys.stdin.readline().rstrip().split()
    dia.add(A and B)

print(len(dia))