import sys
n, m = map(int,input().split())
poket_name = {} # key 값이 str
poket_number = {} # key 값이 int

for i in range (n):
    name = sys.stdin.readline().strip()
    poket_number[i] = name
    poket_name[name] = i

for _ in range (m):
    a = sys.stdin.readline().strip()
    if a.isdigit() == True: # isdigit -> 0(n)
        print(poket_number[int(a)-1])
    else:
        print(poket_name[a]+1)

# isdigit : int를 판별하는 함수 / 숫자 판단하는 함수
# C++의 경우 <cctype>