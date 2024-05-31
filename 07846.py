n = int(input())
arr = [int(i) for i in input().split()]
index = 0
greater = 0

greater = max(arr)

print(max(arr), arr.index(greater) + 1)