n = int(input())
arr = [int(i) for i in input().split()]
max1 = 0
max2 = 0

for i in arr:
    if i == max(arr):
        max1 = i

arr.remove(max1)

for i in arr:
    if i == max(arr):
        max2 = i

print(max1 + max2)