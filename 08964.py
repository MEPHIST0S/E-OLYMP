n = int(input())
arr = [int(i) for i in input().split()]

for i in range(0, n):
    if arr[i] == max(arr):
        arr.insert(n, arr[i])
        arr.remove(arr[i])

for i in arr:
    print(i, end = " ")   