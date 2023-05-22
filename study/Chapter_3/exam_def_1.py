def average_of_4_numbers(num1, num2, num3, num4):
    return (num1 + num2 + num3 + num4) / 4

result = average_of_4_numbers(512,64,256,192)

print(result)


num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))
num3 = float(input("세 번째 숫자를 입력하세요: "))
num4 = float(input("네 번째 숫자를 입력하세요: "))

result = (num1 + num2 + num3 + num4) / 4
print("입력한 숫자들의 평균은", result, "입니다.")


numbers = [float(input(f"{i+1}번째 숫자를 입력하세요: ")) for i in range(4)]
average = sum(numbers) / len(numbers)
print(f"입력한 숫자들의 평균은 {average}입니다.")
