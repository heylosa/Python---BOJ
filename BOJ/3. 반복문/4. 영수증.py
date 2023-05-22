X = int(input())  # 영수증에 쓰여 있는 총 금액
N = int(input())  # 물건의 총 개수

total = 0  # 물건 가격의 총합
for i in range(N):
    a, b = map(int, input().split())
    total += a * b  # 물건 가격 * 물건 개수를 더함

if X == total:
    print("Yes")
else:
    print("No")

    