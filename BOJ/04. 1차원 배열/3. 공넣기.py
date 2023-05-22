n, m = map(int, input().split())
basket = [0] * (n + 1) #1부터 n번까지의 바구니
for _ in range(m):
    i, j, k = map(int, input().split()) #i,j,k 받는다
    for b in range(i, j+1):             #i부터 j번까지 바구니 설정 => b값
        basket[b] = k                   #i부터 j번 바구니까지 k번 공 들여보내
for i in range (1,n+1):                 #1부터 n개 바구니까지 프린트
    print(basket[i], end=' ')