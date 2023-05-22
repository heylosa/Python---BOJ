N,M = map(int,input().split())
basket = [int(i+1) for i in range (N)] #바쿠니 넘버링

for _ in range (M):
    i, j = map(int,input().split()) # i부터 j까지 역순으로 바꾸기
    re = basket[i-1:j]
    re.reverse()
    basket[i-1:j] = re

for i in range(N):
    print(basket[i], end=" ")