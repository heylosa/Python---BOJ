import sys
T = int(sys.stdin.readline())

for _ in range (T):
    word1 = str(input())
    print(f'{word1[0]}{word1[len(word1)-1]}')