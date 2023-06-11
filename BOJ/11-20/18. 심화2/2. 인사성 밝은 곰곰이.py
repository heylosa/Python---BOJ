# 집합 set() 알아두셈.. dictionary는 좀 더 해봐야 될 것 같고
# 집합으로 있냐 없냐 유무 판별하는거는 자주 쓰일 것 같다.

import sys

N = int(input())
gomgom = set()
count_gomgom = 0

for _ in range (N):
    name = sys.stdin.readline().strip()


    if name != 'ENTER':
        if name not in gomgom:
            count_gomgom += 1
            gomgom.add(name)
    elif name == 'ENTER':
        gomgom.clear()

print(count_gomgom)

