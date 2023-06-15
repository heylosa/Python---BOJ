import sys
N = int(input())

dance = set()
dance.add('ChongChong')

for _ in range (N):
    A, B = sys.stdin.readline().strip().split()

    if A in dance:
        dance.add(B)
    if B in dance:
        dance.add(A)

print(len(dance))

# 아래는 해시로 푸는 문제풀이 방법

# 파이썬에는 collections 모듈에 defaultdict 함수가 있다. 이는 모든 해시에 대해 디폴트값을 지정해주는 함수이다.
# defaultdict(bool)로 지정해보자. 그러면 모든 해시에 대해 디폴트 값은 False가 된다.
# 무지개 댄스를 처음부터 추던 ChongChong 의 값만 True로 바꿔주자. 물론, 무지개 댄스를 추는 사람은 1명부터 시작해야 한다.

from collections import defaultdict
dance = defaultdict(bool)
dance['ChongChong'] = True
answer = 1

# 이제 기록을 차례대로 입력받자.
# 두 사람 중 한 사람만 추고 있다면 나머지 사람은 추게 되므로 이를 구현하면 된다.

import sys
input = sys.stdin.readline
from collections import defaultdict

# 총총이는 처음부터 무지개 댄스를 추고 있다.
dance = defaultdict(bool)
dance['ChongChong'] = True
answer = 1

for _ in range(int(input())):
    # A와 B가 만났다.
    A, B = input().split()
    # 두 사람 중 한 사람만 추고 있다면
    # 추고 있지 않은 사람을 추게 만들면 된다.
    if dance[A]:
        if not dance[B]:
            dance[B] = True
            answer += 1
    elif dance[B]:
        dance[A] = True
        answer += 1

print(answer)