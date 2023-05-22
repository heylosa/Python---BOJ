# 매개변수 : 데이터를 전달받기
# 손님이 주문한 음료의 가격을 계산하는 함수를 만들어야 함.
# 주문받은 음료의 내역이 함수 속으로 전달되어야 계산 가능
# 함수에 데이터를 전달하려면 어떻게 해야 할까?
# print() 함수를 호출할 때, print('데이터')와 같이 호출한 것을 기억 << '데이터'가 함수에 전달하는 데이터

def print_price(num_drink):                                             #매개변수(num_drink) 의 정의
    """음료의 잔 수(num_drink)를 전달받아, 가격을 화면에 출력한다."""
    price_per_drink = 2500
    total_price = num_drink * price_per_drink
    print('음료',num_drink, '잔', total_price)

print_price(3)

