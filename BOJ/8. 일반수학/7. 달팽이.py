# 2869
A,B,V = map(int,input().split())

meter = 0
day = 0
while True:
    day += 1
    meter = meter + A
    if meter >= V:
        print(day)
        break
    meter = meter - B


#2 1 6
A, B, V = map(int,input().split())
day = (V-B)/(A-B)
print(int(day) if day == int(day) else int(day)+1)
