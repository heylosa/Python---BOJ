while True:
    N = int(input())
    A = []

    if N == -1:
        break

    for i in range(1, N + 1):
        if N % (i) == 0:
            A.append(i)

    if N == sum(A[0:len(A) - 1]):
        del A[-1]
        B = ' + '.join(str(i) for i in A)
        print(f'{N} = {B}')
    else:
        print(f'{N} is NOT perpect.')
