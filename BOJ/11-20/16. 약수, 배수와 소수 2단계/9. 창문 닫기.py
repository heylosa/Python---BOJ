# 리스트를 이용한 문제풀이 : 메모리 초과
# import sys
# N = int(sys.stdin.readline())
# lst = [1]*N # 입력값의 수만큼 리스트에 1의 개수를 입력 / 1번째 창문여는 것을 생략
#
# if N == 1 or N == 2:
#     print(1)
# else:
#     for i in range (2, N+1):
#         for j in range (i, N+1, i):
#             if lst[j-1] == 0:
#                 lst[j-1] = 1
#             else:
#                 lst[j-1] = 0
#
# print(lst.count(1))

#제곱수를 찾으라는데 ..
# 이것도 시간초과

# import sys
#
# cnt=0
# n = int(sys.stdin.readline())
# for i in range (1, n + 1):
#     if i ** 2 <= n:
#         cnt += 1
# print(cnt)

# [아래 문제 풀이 참고]
# 창문이 열려있으려면 해당 수의 약수의 개수가 홀수개여야 합니다.
# 약수의 개수가 홀수개인 수는 제곱수 밖에 없습니다.
# ex) 1, 4, 9, 16..
# n이하의 제곱수들의 개수를 출력해주면 되는 문제입니다.

N=int(input())
cnt=0
A=1
while(A<=N):
    cnt+=1
    A=(cnt+1)**2
print(cnt)