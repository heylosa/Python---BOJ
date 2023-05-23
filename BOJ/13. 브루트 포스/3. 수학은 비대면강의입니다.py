# 19532 번
# 모든 x와 모든 y를 시도하여 해를 구하는 문제
a, b, c, d, e, f = map(int, input().split())


for i in range (-999, 1000):
    for j in range (-999, 1000):
        if a*i + b*j == c and d*i + e*j == f:
            print(i,j)
            break

# 분수(float)로 들어가면 모든 배수가 성립한다. 때문에 정수로 반환했을 때 같다고 표현해야 함.
# 아래는 처음 잘못적었던 코드, 또 c,f에 0가 입력되면 오류가 나오기 때문에 웬만하면 정수형으로 표현해서 계산하는게 제일 좋음
# k = (a/c-d/f)/(e/f-b/c)
# for i in range (-999, 1000):
#     for j in range (-999, 1000):
#         if k*i == j:
#             print(i,j)
#             break

