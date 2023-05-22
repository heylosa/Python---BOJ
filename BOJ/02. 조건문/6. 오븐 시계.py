hour, minute = map(int,input().split())
time = int(input())

total_minutes = hour * 60 + minute
total_minutes += time

if total_minutes >= 60*24:
    total_minutes -= 24 * 60

new_hour = total_minutes // 60
new_minute = total_minutes % 60

print(new_hour, new_minute)