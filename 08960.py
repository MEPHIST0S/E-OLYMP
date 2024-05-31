n = int(input())
arr = [int(i) for i in input().split()]
greatest = max(arr)
lowest = min(arr)
res = 0

for i in arr:
    if i != greatest and i != lowest:
        res += i

print(res)