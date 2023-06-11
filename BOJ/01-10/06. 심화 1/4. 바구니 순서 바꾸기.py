import sys

N, M = map(int,sys.stdin.readline().split()) # N개의 바구니, M개의 줄
basket = [int(i+1) for i in range (N)] #바구니 넘버링 1~N
# basket = [0] * (n + 1)   #1부터 n번까지의 바구니

# i,j,k = i번째 바구니 부터 j번째 바구니의 순서를 회전시키는데, 그때 기준 바구니는 k번째 바구니 ( 1 <= i <= k <= j <= N )
# i가 begin, j가 end, k가 mid.
# i -k , k - j == k -j + i - k


for _ in range (M):
    i, j, k = map(int, sys.stdin.readline().split())
    basket = basket[:i-1] + basket[k-1:j] + basket[i-1:k-1] + basket[j:]
print(*basket)

# i부터 j까지 리스트 불러와서 k부터 j까지 넣고 i 부터 k까지 연속으로 넣으면 된다.
# 이거 10번 반복

# 이상 / 미만

#1,2,3,4,5,6,7,8,9,10
#1 4 6 2 3 7 10 5 8 9