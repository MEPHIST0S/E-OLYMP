n = int(input())
arr = []
for _ in range (n):
    arr.append(int(input()))

def Reverse(n, arr):
    arr_new = []
    for i in range(n):
        arr_new.append(arr[n-1-i])
    return arr_new

print(*Reverse(n, arr))