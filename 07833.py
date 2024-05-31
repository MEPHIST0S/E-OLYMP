n = int(input())
arr = [int(i) for i in input().split()]
avrg = 0
sum = 0
count = 0

for i in arr:
    avrg += i
avrg = avrg/n

for i in arr:
    if avrg < i:
        sum += i
        count += 1

print(sum, count)