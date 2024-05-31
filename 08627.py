arr = [int(i) for i in input().split()]
res = [0] * len(arr)

for i in range(1, len(arr)-1):
    res[i] = arr[i - 1] + arr[i + 1]

res[0] = arr[0]
res[-1] = arr[-1]

for i in res:
    print(i, end = " ")