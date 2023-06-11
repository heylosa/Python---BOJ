
while 1:
    try:
        A, B = map(int,input().split())
        if B % A == 0 and A % B == A:
            print('factor')
        elif A % B == 0 and B % A == B:
            print('multiple')
        elif A ==0 and B ==0:
            break
        else:
            print('neither')
    except:
        break
