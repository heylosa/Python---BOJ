import sys


def recursion(s, l, r):
    global N
    N += 1

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())

for _ in range (T):
    N = 0
    print(isPalindrome(sys.stdin.readline().rstrip()), N)
    #rstrip을 가야하는 이유. sys.stdin.readline() 같은 경우 개행문자 \n이 포함되기 때문에 이 공백을 없애줘야함
