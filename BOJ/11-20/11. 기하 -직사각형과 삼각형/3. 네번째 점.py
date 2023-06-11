X = []
Y = []

for _ in range (3):
    A, B = map(int,input().split())
    X.append(A)
    Y.append(B)

for i in range (3):
    if X.count(X[i]) == 1:
        x = X[i]
    if Y.count(Y[i]) == 1:
        y = Y[i]
print(x, y)