n = int(input())

for i in range(1, n + 1):
    if i % 2 == 1:
        if n % i == 0:
            print(i)