n = int(input())
count = 0
i = 1
arr = list()

while count < n:
    if (i % 2 != 0 and i % 5 != 0 and i % 3 != 0):
        arr.append(i)
        count += 1
    i += 1 

for i in arr:
    print(i, end = " ")