# 메모리를 최소화 시키려면 for문 안에서 반복수행하는 부분들을 최소화시켜야 한다.
# input()은 개행문자를 삭제하고 반환하기 때문에 한 단계의 과정이 더 존재해서 sys.stdin.readline 시간이 보다 더 오래 걸리게 된다
# 파이썬은 미리 만들어놓은 곳에 단순한 계산이 들어가면 시간이 확연하게 단축되기 때문에 이런 점을 고려해서
# 메모리 / 계산시간을 줄이는 코드를 짜야 효율적이다.

# 아래는 카운팅정렬 방법이다.
# 범위내의 list/배열을 설정해놓ㄱ, 입력받을 때 마다 그 수에 해당하는 인덱스에 +1을 해주는 것.



import sys

n = int(sys.stdin.readline())
list = [0] * 10001

for i in range (n):
    list[int(sys.stdin.readline())] += 1

for i in range (10001):
    if list[i] != 0:
        for j in range (list[i]):
            print(i)
