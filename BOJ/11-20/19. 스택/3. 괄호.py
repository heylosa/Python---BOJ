# 9012
# 주어진 문자열이 올바른 괄호열인지 판단하는 문제
import sys
T = int(input())
for _ in range (T):
    str = sys.stdin.readline().rstrip()
    stack = []
    isVPS = True    # 괄호의 유무를 표현하는 것, False는 초기화

    for i in str:
        if i == "(":
            stack.append("(")
        if i == ")":
            if stack:
                stack.pop()
            elif not stack:
                isVPS = False
                break
    if not stack and isVPS: # 아래부분이 이해가 안되는데
        print("YES")
    elif stack or not isVPS:
        print("NO")


#pop, append 의 시간복잡도는 O(1)
# 문자열을 한 글자씩 검사해서 여는 괄호이면 스택에 넣고,
# 닫는 괄호이면 스택을 pop()한다. 이때 pop()할 원소가 없다면 열지도 않은 괄호를 닫은 것이기에
# 불리언 값을 False로 초기화하고 반복문을 탈출한다. 또 모든 검사가 끝났을 때 스택에
# 원소가 남아있으면 여는 괄호가 모두 닫히지 않은 것이기에 False로 초기화한다.
# 스택에 원소가 없고 isVPS가 True이면 'YES'를, 그렇지 않으면 'NO'를 출력한다.