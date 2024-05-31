n = int(input())
count = 0
for i in range(1, n+1):
    if n % i == n // i:
        count += 1
print(count)