H, M = map(int,input().split())

if M-45 < 0:
    M = M*(-1)

print(H, M)


# M이 문자열이라면? 입력받은게 45번이고 여기서 범위를 0<= M <=59 로 설정해놓는다면 뺴기하면 알아서 뒤로감
# H도 문자열이라면 0<= H <=23 으로 설정해놓는다.
# 입력시간을 24시간 표현을 사용한다면? clock 관련 함수가 있을 것 같음

hour, minute = map(int,input().split())

total_minutes = hour * 60 + minute
total_minutes -= 45

if total_minutes < 0:
    total_minutes += 24 * 60

new_hour = total_minutes // 60
new_minute = total_minutes % 60

print(new_hour, new_minute)