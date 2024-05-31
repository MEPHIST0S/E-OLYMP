n = int(input())
arr = list(map(int, input().split()))
unique = list()


for i in arr:
    if arr.count(i) == 1:
        unique.append(i)

for i in unique:
    print(i, end = " ")