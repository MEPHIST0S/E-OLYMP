n = int(input())
arr = list(map(int, input().split()))
greatest = max(arr)/2
lowest = min(arr)/2

for i in range(len(arr)):
    if arr[i] > 0:
        arr[i] -= int(greatest)
    elif arr[i] < 0:
        arr[i] -= int(lowest)

print(*arr)