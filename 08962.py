n = int(input())
arr = list(map(int, input().split()))
greatest = max(arr)
igreatest = arr.index(greatest)
index = igreatest

for i in range(igreatest + 1, n):
    if arr[i] == greatest:
        index = i 


arr[index] = arr[-1]
arr[-1] = greatest

for i in arr:
    print(i, end = " ")