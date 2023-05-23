# 2839번
# 한때는 이 문제가 "기본 수학 1" 단계에 있었지만, 사실 브루트 포스로 푸는 게 더 쉽습니다.
N = int(input())
k = N // 5

while True:
    if k == 0:
        print(-1)
        break

    elif k > 0:
        for i in range(k + 1):
            M = N - 5*(k-i)
            if M % 3 == 0:
                print((k-i) + ((M) // 3))
                break
            elif i == k:
                if M % 3 > 0:
                    print(-1)
                    break
        break
