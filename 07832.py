n = int(input())
arr = [int(i) for i in input().split()]
count = 0

for i in arr:
    if i == max(arr):
        count += 1

print(count)