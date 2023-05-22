# 5622번 다이얼
# 1. 각 알파벳에 해당하는 걸리는 시간을 그룹화
# ABC : 3s, DEF : 4s, GHI : 5s, JKL : 6s, MNO : 7s, PQRS : 8s, TUV : 9s, WXYZ : 10s
# 각 인덱스는 0 , 1 ,2 3, 4, 5, 6, 7 ~ 으로 되니까 최종적으로 해당 인덱스에 +3만 하면 된다.
# 2. 입력값에 포함되는 알파벳들을 숫자로 치환해서 더한다.

dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = list(input())

number = 0
for i in range(len(word)): #만약 입력값이 WA 라면 len(word)는 문자열 길이 2이다. 때문에 0 ~ 1 까지 i값이 결정됨
    for k in dial:
        if word[i] in k:
            number += dial.index(k) + 3

print(number)


# 여기서 W에 해당하는 값은 10의 값이 주어지고 이 값은 dial의 index 값이어야 한다.
# dial에 W에 해당하는 index를 구하기 위해서는 W가 dial의 어디에 속해있는지 알아야하고, 이것은 해당 인덱스를 쪼개서 비교해야한다?