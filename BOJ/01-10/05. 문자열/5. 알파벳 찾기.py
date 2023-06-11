# 하나 받고, A-Z 까지 ALL 26개다 검사, if S에 A-Z 있으면 A-Z list 받고 해당 index(i)

S = list(input())
list = list("abcdefghijklmnopqrstuvwxyz")

for i in list:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')
