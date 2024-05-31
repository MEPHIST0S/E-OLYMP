n = int(input())
arr = [int(i) for i in input().split()]

for i in range(0, n-1):
    if ((arr[i] > 0 and arr[i + 1] > 0) or
        (arr[i] < 0 and arr[i + 1] < 0)):
        print(arr[i], arr[i + 1])