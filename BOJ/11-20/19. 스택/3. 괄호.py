# 9012
# 주어진 문자열이 올바른 괄호열인지 판단하는 문제
import sys
T = int(input())
for _ in range (T):
    str = sys.stdin.readline().rstrip()
    for _ in range (int(len(str)/2)):
        str.replace('()','')
        print(str)
    if str == '':
        print("YES")
    else:
        print("NO")

