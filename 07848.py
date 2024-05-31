n = int(input())
arr = [int(i) for i in input().split()]
clone = 0


for i in range(0, n-1, 2):
    clone = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = clone

for i in arr:
    print(i)