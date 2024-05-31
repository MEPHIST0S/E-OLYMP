n = int(input())
arr = [int(i) for i in input().split()]
max = arr[0]

for i in arr:
    if i > max:
        max = i

print(max)