# 큰 배열이 있을 때 효율적으로 비교 탐색이 가능한가를 묻는 문제.
# 속도는 dictionary
# Q1: dictionary 활용

import sys

N = int(input())
A = list(sys.stdin.readline().split())
M = int(input())
B = list(sys.stdin.readline().split())

A_dictionary = {}
for i in range (len(A)):
    A_dictionary[A[i]] = 0 #아무숫자 mapping한다네요

for i in range (M):
    if B[i] in A_dictionary:
        print(1, end= ' ')
    else:
        print(0, end= ' ')

# Q2: 이진탐색 인터넷 참고
# 1. 가지고 있는 cards를 sort 시킨다.
# 2. 체크할 배열 checks에서 check를 하나씩 꺼내면서
# 3. 이진 탐색을 위한 low, high, mid를 지정
# 4. cards의 중간 index와 비교한다.
# 5. check가 중간 값보다 작다면, 왼쪽 한 칸 옆까지 탐색하게 high를 조정
# 6. check가 중간 값보다 크다면, 오른쪽 한 칸 옆부터 탐색하게 low를 조정
# 7. check가 중간 값과 일치하면 바로 멈추고 1 출력
# 8. 끝까지 없다면 (exist = 그대로 False) 0 출력

import sys

N = int(input())
A = sorted(list(sys.stdin.readline().split())) #가지고 있는 card 정렬조져
M = int(input())
B = list(sys.stdin.readline().split()) #체크해야할 card 목록 B가 A에 있는지 확인해야함

for i in B:
    low, high = 0, N-1 #가지고있는 card A의 이진 탐색 index / 최소값, 최고값 설정
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if A[mid] > i: # 중간값보다 작으면 중간보다 왼쪽 한 칸 옆까지 탐색
            high = mid - 1
        elif A[mid] < i: # 중간값보다 크면 중간보다 오른쪽 한 칸 옆부터 탐색
            low = mid + 1
        else:
            exist = True
            break
    print(1 if exist else 0, end= ' ')