n = int(input())
arr = list(map(int, input().split()))
lowest = min(arr)
clone = list()

for i in arr:
    if i == lowest:
        clone.append(i)

for i in arr:
    if i != lowest:
        clone.append(i)

print(*clone)