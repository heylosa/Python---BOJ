# 독스트링 : 함수가 하는 일 설명하기
# 파이썬에서는 함수를 정의할 때 함수에 관한 설명을 작성해 둘 수 있다 => 독스트링 (Docstring)
# 독스트링은 def 문에서 헤더행 바로 다음 행에 큰따옴표 세 개로 감싸 적는다
# ex)
# def Function_name():
#    """Docstring"""
#     main

def order():
    """사용자로부터 주문할 음료를 입력받아, 주문사항을 화면에 출력한다."""
    print('주문하실 음료를 알려주세요')
    drink = input()
    print(drink, '주문하셨습니다.')

order()
    # Help() 함수가 보여주는 것이 독스트링이다.