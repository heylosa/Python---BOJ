import sys

N = int(input())
A = list(sys.stdin.readline().split())
M = int(input())
B = list(sys.stdin.readline().split())

c0unt = {} #dictionary 설정
for i in A: # A는 가지고 있는 카드, A의 첫번째 부터 dictionary 에 있다면 +1 넣고, 없다면 1로 설정해주면서 값을 부여 / counting 시작
    if i in c0unt:
        c0unt[i] += 1
    else:
        c0unt[i] = 1

for i in B: # B는 검사할 카드, B의 첫번째 부터 c0unt에 존재한다면 c0unt의 i를 출력 / 어차피 숫자니까 해당 숫자위치의 dictionary가 저장됨
    if i in c0unt:
        print(c0unt[i], end=' ')
    else:
        print(0, end=' ')