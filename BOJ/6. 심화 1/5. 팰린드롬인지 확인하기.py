word = input()
contrast = word[::-1]
if word == contrast:
    print("1")
else:
    print("0")