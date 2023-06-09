import sys
N=int(sys.stdin.readline())

def ch(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

for _ in range(N):
    i=int(sys.stdin.readline())
    while True:
        if i==0 or i==1:
            print(2)
            break
        if ch(i):
            print(i)
            break
        else:
            i+=1