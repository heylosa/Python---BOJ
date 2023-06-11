n = int(input())

for i in range (n):
    space = ' '*(n-1)
    star = '*'
    i += 1
    n -= 1
    print(space + star*i)


# 만약 n 이 5라면
# 공백 4개 별 1개
# 공백 3개 별 2개
# 공백 2개 별 3개
# 공백 2개 별 4개
# 공백 0개 별 5개

# space is n-1
# star i~n 공백 이후에 체크