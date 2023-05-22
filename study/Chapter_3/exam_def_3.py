def triangle_area(base, height):
    return base * height / 2

base = int(input("삼각형의 밑변을 입력하세요: "))
height = int(input("삼각형의 높이를 입력하세요: "))
area = triangle_area(base, height)

print(f"밑변이 {base}이고 높이가 {height}인 삼각형의 넓이는 {area}입니다.")



