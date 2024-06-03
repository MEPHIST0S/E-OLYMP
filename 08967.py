n = int(input())
arr = [int(i) for i in input().split()]
diff = max(arr) - min(arr)

for i in range(len(arr)):
    arr[i] -= int(diff)

print(*arr)