n = int(input())
max = 0
for digit in str(n):
    if int(digit) > max:
        max = int(digit)

print(max)