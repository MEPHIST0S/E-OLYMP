n = int(input())
arr = [int(i) for i in input().split()]
greatest = max(arr)
lowest = min(arr)

for i in range(0, n):
    if arr[i] == greatest:
        arr[i] = lowest
    elif arr[i] == lowest:
        arr[i] = greatest

for i in arr:
    print(i, end = " ")