def order():                                    #헤더 행
    print('주문하실 음료를 알려주세요')             #본문 코드 블록
    drink = input()
    print(drink, '주문하셨습니다')

order()                                     #여기에는 들여쓰기 안함 // 함수를 호출해야 실행 된다.

def print_absolute():
    print('정수를 입력하세요')
    number = int(input())
    print(number,'의 절대값:',abs(number))

print_absolute()

