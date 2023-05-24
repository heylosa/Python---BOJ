# 2839번
# 한때는 이 문제가 "기본 수학 1" 단계에 있었지만, 사실 브루트 포스로 푸는 게 더 쉽습니다.
N = int(input())
k = N // 5


if k == 0 and N != 3:
    print(-1)


else:
    for i in range(k + 1):
        if (N - 5 * (k - i)) % 3 == 0:
            print((k - i) + ((N - 5 * (k - i)) // 3))
            break

        elif N == 3:
            print(1)
            break
