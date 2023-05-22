def print_order(drink, cake):            # ❶ 콤마(,)로 구분해 매개변수 여러 개 정의
    """음료(drink)와 케익을(cake)를 전달받아, 주문 내용을 화면에 출력한다."""
    print('음료:', drink, '/', '케익:', cake)

print_order('카페라테', '치즈케익')      # ❷ 함수에 여러 개의 인자를 전달하여 호출하기
print_order('당근케익', '우유')          # ❸ 전달하는 인자의 순서에 주의하자!




def price(num_drink):
    """음료의 잔 수(num_drink)을 전달받아, 가격을 반환한다."""
    price_per_drink = 2500
    total_price = num_drink * price_per_drink
    return total_price                         # ❶ 계산한 값 반환하기 => ??

result = price(3)                              # ❷ 함수 호출하고 반환값 저장하기
print('가격:', result)