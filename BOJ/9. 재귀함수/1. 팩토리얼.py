def fin(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* fin(n-1)
print(fin(int(input())))
