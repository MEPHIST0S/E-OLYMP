#Solution - 1 (76%)
a, b = map(int, input().split())
sum = 0

for i in range(a, b+1):
    if abs(i) % 2 == 1:
        sum += i

print(sum)