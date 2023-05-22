import sys

T = int(sys.stdin.readline())

for _ in range (T):
    N = int(sys.stdin.readline())
    Q = N // 25
    D = (N-25*Q) // 10
    Ni = ((N-25*Q)-10*D) // 5
    P = ((N-25*Q)-10*D)-5*Ni // 1
    print (Q,D,Ni,P)
