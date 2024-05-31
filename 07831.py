n = int(input())
arr = [int(i) for i in input().split()]

res = 0

for i in arr:
    if i != max(arr):
        res += i

print(res)