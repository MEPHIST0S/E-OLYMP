n = int(input())
arr = [int(i) for i in input().split()]

for i in range (1, n):
    if arr[i] > arr[i-1]:
        print(arr[i])