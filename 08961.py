n = int(input())
arr = list(map(int, input().split()))
lowest = min(arr)
ilowest = arr.index(lowest)

arr[ilowest] = arr[0]
arr[0] = lowest

for i in arr:
    print(i, end = " ")