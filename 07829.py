n = int(input())

arr = [float(i) for i in input().split()]

sum = 0
for i in arr:
    sum += i

print("{:.1f}".format(sum))