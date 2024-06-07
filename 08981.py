text = input()

first = text.find(' ')
last = text.rfind(' ')

if first == -1:
    print(-1)
else:
    print(first, last)