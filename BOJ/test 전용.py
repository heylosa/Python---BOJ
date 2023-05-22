def draw_stars(n, x, y):
    # base case: n이 1일 때, 별을 출력하고 종료
    if n == 1:
        stars[y][x] = '*'
        return

    # 재귀적으로 패턴을 그리는 부분
    div = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                # 가운데 부분은 공백으로 남기기
                continue
            draw_stars(div, x + j * div, y + i * div)

# 입력 받기
N = int(input())

# N x N 크기의 2차원 리스트 생성
stars = [[' '] * N for _ in range(N)]

# 별 그리기 함수 호출
draw_stars(N, 0, 0)

# 별 출력
for row in stars:
    print(''.join(row))
