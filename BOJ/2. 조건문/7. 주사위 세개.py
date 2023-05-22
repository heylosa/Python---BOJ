a, b, c = map(int, input().split())

if a == b == c:
    prize = 10000 + a * 1000
elif a == b or a == c or b == c:
    same_eye = a if a == b or a == c else b
    prize = 1000 + same_eye * 100
else:
    prize = max(a, b, c) * 100

print(prize)