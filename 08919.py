n = int(input())
for i in range(1, int(n**(1/3)) + 1):
    if i**3 < n:
        print(i**3, end = " ")