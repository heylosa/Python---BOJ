while True:
    A, B, C = map(int,input().split())
    N =[]
    N.append(A)
    N.append(B)
    N.append(C)
    sorted(N)
    if sum(N) == 0:
        break
    elif  N[0] + N[1] > N[2]:
        if A == B == C:
            print('Equilateral')
        elif A == B or B == C or C == A:
            print('Isosceles')
        elif A != B != C:
            print('Scalene')
    elif N[0] + N[1] <= N[2]:
        print('Invalid')
    else:
        break


