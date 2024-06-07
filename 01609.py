n = input()
a = input()
count = 0

for digit in n:
    if digit == '-' or digit == '+':
        continue
    if digit == a:
        count += 1

print(count)