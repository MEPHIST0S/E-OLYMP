n = int(input())
arr = list(map(int, input().split()))
clone = [0] * n

if n % 2 == 0:
    even = n // 2
else:
    even = (n // 2) + 1

arr_even = arr[:even]
arr_odd = arr[even:]

for i in range(even):
    clone[2 * i] = arr_even[i]

for i in range(n // 2):
    clone[2 * i + 1] = arr_odd[i]

print(*clone)