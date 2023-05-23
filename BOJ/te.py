for N in range (1, 5001):
    k = N // 5

    if k == 0:
        print(-1)

    elif k > 0:
        for i in range(k + 1):
            M = N - 5*(k-i)
            if M % 3 == 0:
                print((k-i) + ((M) // 3))
                break
            elif i == k:
                if M % 3 > 0:
                    print(-1)