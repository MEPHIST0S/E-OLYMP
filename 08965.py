n = int(input())
arr = list(map(int, input().split()))
lowest = min(arr)/2

for i in range(len(arr)):
    arr[i] -= int(lowest)

print(*arr)