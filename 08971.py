n = int(input())
arr = list(map(int, input().split()))
unique = list()

for i in arr:
    if i not in unique:
        unique.append(i)

for i in unique:
    print(i, end = " ")