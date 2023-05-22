N, M = map(int,input().split())
basket = [int(i+1) for i in range (N)] #바구니 넘버링 1~N
for _ in range (M):
    i, j = map(int,input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for i in range (N):
    print(basket[i],end=" ")
