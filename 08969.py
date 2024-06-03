n = int(input())
arr = [int(i) for i in input().split()]
clone = [0] * n
clone[0] = arr[0]

for i in range(1, len(arr)):
    clone[i] = arr[i] - arr[i-1]

print(*clone)