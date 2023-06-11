x, y, w, h = map(int,input().split())
A = []
A.append(w-x)
A.append(h-y)
A.append(x)
A.append(y)
print(min(A))