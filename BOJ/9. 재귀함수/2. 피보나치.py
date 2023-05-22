def fin(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        return fin(n-2) + fin(n-1)

print(fin(int(input())))
